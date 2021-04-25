import os
import json
import base64
import pandas as pd
import streamlit as st

from app.data_extractor.operations import ProcessFingerprint

def _bin_downloader(bin_file_path, file_label='File'):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file_path)}">Download {file_label}</a>'
    return href

def app():
        #@ ----------------------------------------------------------------------------------------------------------
        #@ Page title
        st.markdown("""# **Extract Data**""")

        example_fp_path = './app/data_extractor/examples/example_fp.csv'
        example_cntb_path = './app/data_extractor/examples/example_contribution.csv'

        outputcsvpath = './app/data_extractor/data/output_dataframe.csv'
        outputjsonpath  = './app/data_extractor/data/data.json'

        #@ ----------------------------------------------------------------------------------------------------------

        with st.sidebar.header('Upload your CSV data'):

            delimiter_dict = {',':',', ';':';'}
            user_delimiter = st.sidebar.selectbox('Choose CSV file delimiter', list(delimiter_dict.keys()))
            selected_delimiter = delimiter_dict[user_delimiter]

            uploaded_FP = st.sidebar.file_uploader("Upload fingerprint data file (CSV)", type=["csv"])
            st.sidebar.markdown(_bin_downloader(example_fp_path, 'fingerprint csv example'), unsafe_allow_html=True)

            # uploaded_CNT = st.sidebar.file_uploader("Upload contribution data file (CSV)", type=["csv"])
            # exemple_CNT = pd.read_csv(example_cntb_path, delimiter=',')
            # st.sidebar.markdown(_fileDownload(exemple_CNT, 'example_cntb', 'Download contribution csv example'), unsafe_allow_html=True)
            
            # if uploaded_CNT is not None:
            # inputcontribution = pd.read_csv(uploaded_CNT, index_col=0, delimiter=selected_delimiter)
            # contribution = st.sidebar.slider('Contribution threshold', min_value=0.0, max_value=1.0, value=0.6, step=0.1)
            # st.info(f'Contribution threshold: {contribution}')

        if uploaded_FP is None:
            st.info('Awaiting file to be uploaded.')

        if uploaded_FP is not None:
            inputdataframe = pd.read_csv(uploaded_FP, index_col=0, delimiter=selected_delimiter)
            variance = st.sidebar.slider('Variance threshold', min_value=0.0, max_value=1.0, value=0.8, step=0.1)
            minmargin = st.sidebar.slider('Min search tolerance', min_value=0.0, max_value=1.0, value=0.3, step=0.1)
            maxmargin = st.sidebar.slider('Max search tolerance', min_value=0.0, max_value=1.0, value=0.3, step=0.1)

            st.info(f'Variance threshold: {variance}')
            st.info(f'Min search tolerance: {minmargin}')
            st.info(f'Max search tolerance: {maxmargin}')

            if st.button('Calculate'):
                compute = ProcessFingerprint(inputdataframe, variance, minmargin,
                                        maxmargin, False, outputcsvpath, outputjsonpath)

                with st.spinner('Calculating data...'):
                    compute.execute()
                st.success(f'Done!')
                st.markdown(_bin_downloader(outputjsonpath, 'processed data'), unsafe_allow_html=True)
