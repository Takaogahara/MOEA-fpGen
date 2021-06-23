# External imports
import json
import streamlit as st

# Local imports
from app.optimizer.core import Optimizer
from app.commons import Sidebar, bin_downloader

EXAMPLE_JSON_PATH = './app/optimizer/examples/example_json.json'
RESULT_PATH = './app/optimizer/data/generated_fp.csv'

POP_SIZE = None
N_PARTITIONS = None
N_NEIGHBORS = None


def app():
    """
    Generate streamlit interface
    """

    st.markdown("""# **Generator**""")

    selected_method = {}
    # @ --------------------------------------------------------------------
    # @ Sidebar

    with st.sidebar.header('Upload your CSV data'):
        uploaded_file = Sidebar.sidebar_uploader(text='Upload data file \
                                                (JSON)',
                                                 extension='json',
                                                 file_path=EXAMPLE_JSON_PATH,
                                                 exemple_text='Download \
                                                 json data example')

    if uploaded_file is None:
        st.info('Awaiting file to be uploaded.')

    if uploaded_file is not None:
        data = json.load(uploaded_file)

        N_VAR = len(list(data['min'][0]['active'].values()))
        N_OBJ = 2
        N_CONSTR = 2
        N_GEN = st.sidebar.slider('Generations', min_value=10, max_value=1000,
                                  value=100, step=10)

        function_dict = {'Fixed mean': 'Fixed mean',
                         'Variable mean': 'Variable mean'}
        selected_function = Sidebar.sidebar_dict_select(function_dict,
                                                        'Choose optimization \
                                                        problem')

        algorithm_dict = {'NSGA2': 'NSGA2', 'NSGA3': 'NSGA3',
                          'MOEA/D': 'MOEA/D', 'C-TAEA': 'C-TAEA'}
        selected_algorithm = Sidebar.sidebar_dict_select(algorithm_dict,
                                                         'Choose optimization \
                                                         algorithm')

        if selected_algorithm == 'NSGA2':
            POP_SIZE = st.sidebar.slider('Population number', min_value=10,
                                         max_value=200, value=100, step=10)

            selected_method = {'algorithm': 'NSGA2', 'parameters': POP_SIZE}

        if selected_algorithm == 'NSGA3':
            POP_SIZE = st.sidebar.slider('Population number', min_value=10,
                                         max_value=200, value=100, step=10)

            N_PARTITIONS = st.sidebar.slider('Pratitions number', min_value=0,
                                             max_value=20, value=12, step=1)

            selected_method = {'algorithm': 'NSGA3',
                               'parameters': (POP_SIZE, N_PARTITIONS)}

        if selected_algorithm == 'MOEA/D':
            N_NEIGHBORS = st.sidebar.slider('Neighbors number', min_value=0,
                                            max_value=25, value=15, step=1)

            N_PARTITIONS = st.sidebar.slider('Pratitions number', min_value=0,
                                             max_value=20, value=12, step=1)

            selected_method = {'algorithm': 'MOEA/D',
                               'parameters': (N_NEIGHBORS, N_PARTITIONS)}

        if selected_algorithm == 'C-TAEA':
            N_PARTITIONS = st.sidebar.slider('Pratitions number', min_value=0,
                                             max_value=20, value=12, step=1)

            selected_method = {'algorithm': 'C-TAEA',
                               'parameters': N_PARTITIONS}

        st.info(f'Number of variables (fingerprint): {N_VAR}')
        st.info(f'Optimization problem: {selected_function}')
        st.info(f'Optimization algorithm: {selected_algorithm}')
        st.info(f'Generations: {N_GEN}')

        if POP_SIZE is not None:
            st.info(f'Population number: {POP_SIZE}')
        if N_PARTITIONS is not None:
            st.info(f'Pratitions number: {N_PARTITIONS}')
        if N_NEIGHBORS is not None:
            st.info(f'Neighbors number: {N_NEIGHBORS}')

        if st.button('Generate!'):
            compute = Optimizer(N_VAR, N_OBJ, N_CONSTR, N_GEN,
                                selected_method, data, RESULT_PATH,
                                selected_function)

            with st.spinner('Generating fingerprints...'):
                compute.execute()

            st.success('Done!')
            st.markdown(bin_downloader(RESULT_PATH, 'processed data'))
