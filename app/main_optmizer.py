import os
import json
import base64
import pandas as pd
import streamlit as st

from app.optimizer.core import Optimizer

def _bin_downloader(bin_file_path, file_label='File'):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file_path)}">Download {file_label}</a>'
    return href

def app():
        #@ ----------------------------------------------------------------------------------------------------------
        #@ Page title
        st.markdown("""# **Generator**""")

        EXAMPLE_JSON_PATH = './app/optimizer/examples/example_json.json'
        RESULT_PATH = './app/optimizer/output/generated_fp.csv'

        POP_SIZE = None
        N_PARTITIONS = None
        N_NEIGHBORS = None
        selected_method = {}
        #@ ----------------------------------------------------------------------------------------------------------
        #@ Sidebar

        with st.sidebar.header('Upload your CSV data'):
            uploaded_file = st.sidebar.file_uploader("Upload data file (JSON)", type=["json"])
            st.sidebar.markdown(_bin_downloader(EXAMPLE_JSON_PATH, 'json data example'), unsafe_allow_html=True)


        if uploaded_file is None:
            st.info('Awaiting file to be uploaded.')

        if uploaded_file is not None:
            data = json.load(uploaded_file)
            N_VAR = len(list(data['min'][0]['active'].values()))
            N_OBJ = 2
            N_CONSTR = 2

            N_GEN = st.sidebar.slider('Generations', min_value=10, max_value=1000, value=100, step=10)
            algorithm_dict = {'NSGA2':'NSGA2', 'NSGA3':'NSGA3', 'MOEA/D':'MOEA/D', 'C-TAEA':'C-TAEA'}
            user_algorithm = st.sidebar.selectbox('Choose optimization algorithm', list(algorithm_dict.keys()))
            selected_algorithm = algorithm_dict[user_algorithm]

            if selected_algorithm == 'NSGA2':
                POP_SIZE = st.sidebar.slider('Population number', min_value=10, max_value=200, value=100, step=10)
                selected_method = {'algorithm':'NSGA2', 'parameters':POP_SIZE}

            if selected_algorithm == 'NSGA3':
                POP_SIZE = st.sidebar.slider('Population number', min_value=10, max_value=200, value=100, step=10)
                N_PARTITIONS = st.sidebar.slider('Pratitions number', min_value=0, max_value=20, value=12, step=1)
                selected_method = {'algorithm':'NSGA3', 'parameters':(POP_SIZE, N_PARTITIONS)}

            if selected_algorithm == 'MOEA/D':
                N_NEIGHBORS = st.sidebar.slider('Neighbors number', min_value=0, max_value=25, value=15, step=1)
                N_PARTITIONS = st.sidebar.slider('Pratitions number', min_value=0, max_value=20, value=12, step=1)
                selected_method = {'algorithm':'MOEA/D', 'parameters':(N_NEIGHBORS, N_PARTITIONS)}

            if selected_algorithm == 'C-TAEA':
                N_PARTITIONS = st.sidebar.slider('Pratitions number', min_value=0, max_value=20, value=12, step=1)
                selected_method = {'algorithm':'C-TAEA', 'parameters':N_PARTITIONS}


            st.info(f'Number of variables (fingerprint): {N_VAR}')
            st.info(f'Optimization algorithm: {selected_algorithm}')
            st.info(f'Generations: {N_GEN}')

            if POP_SIZE is not None:
                st.info(f'Population number: {POP_SIZE}')
            if N_PARTITIONS is not None:
                st.info(f'Pratitions number: {N_PARTITIONS}')
            if N_NEIGHBORS is not None:
                st.info(f'Neighbors number: {N_NEIGHBORS}')



            if st.button('Generate!'):
                compute = Optimizer(N_VAR, N_OBJ, N_CONSTR, N_GEN, selected_method, data, RESULT_PATH)

                with st.spinner('Generating fingerprints...'):
                    compute.execute()
                st.success(f'Done!')
                st.markdown(_bin_downloader(RESULT_PATH, 'processed data'), unsafe_allow_html=True)