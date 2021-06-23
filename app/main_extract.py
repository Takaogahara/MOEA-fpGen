# External imports
import pandas as pd
import streamlit as st

# Local imports
from app.data_extractor.operations import ProcessFingerprint
from app.commons import Sidebar, bin_downloader


EXAMPLE_FP_PATH = './app/data_extractor/examples/example_fp.csv'
EXAMPLE_CNTB_PATH = './app/data_extractor/examples/example_contribution.csv'

OUTPUTCSVPATH = './app/data_extractor/data/output_dataframe.csv'
OUTPUTJSONPATH = './app/data_extractor/data/data.json'


def app():
    """
    Generate streamlit interface
    """

    st.markdown("""# **Data Extractor**""")

    # @ -----------------------------------------------------------------------

    with st.sidebar.header('Upload your CSV data'):

        delimiter_dict = {',': ',', ';': ';'}
        selected_delimiter = Sidebar.sidebar_dict_select(delimiter_dict,
                                                         'Choose CSV file \
                                                          delimiter')

        uploaded_FP = Sidebar.sidebar_uploader(text='Upload fingerprint \
                                               data file (CSV)',
                                               extension='csv',
                                               file_path=EXAMPLE_FP_PATH,
                                               exemple_text='fingerprint\
                                               csv example')

        # uploaded_CNT = Sidebar.sidebar_uploader(text='Upload contribution \
        #                                        data file (CSV)',
        #                                         extension='csv',
        #                                         file_path=EXAMPLE_CNTB_PATH,
        #                                         exemple_text='Download \
        #                                         contribution csv example')

        # if uploaded_CNT is not None:
        # inputcontribution = pd.read_csv(uploaded_CNT, index_col=0,
        #                                 delimiter=selected_delimiter)
        # contribution = st.sidebar.slider(
        #     'Contribution threshold', min_value=0.0, max_value=1.0,
        #     value=0.6, step=0.1)

        # st.info(f'Contribution threshold: {contribution}')

    if uploaded_FP is None:
        st.info('Awaiting file to be uploaded.')

    if uploaded_FP is not None:
        inputdataframe = pd.read_csv(uploaded_FP, index_col=0,
                                     delimiter=selected_delimiter)

        variance = st.sidebar.slider('Variance threshold', min_value=0.0,
                                     max_value=1.0, value=0.8, step=0.1)

        minmargin = st.sidebar.slider('Min search tolerance', min_value=0.0,
                                      max_value=1.0, value=0.3, step=0.1)

        maxmargin = st.sidebar.slider('Max search tolerance', min_value=0.0,
                                      max_value=1.0, value=0.3, step=0.1)

        st.info(f'Variance threshold: {variance}')
        st.info(f'Min search tolerance: {minmargin}')
        st.info(f'Max search tolerance: {maxmargin}')

        if st.button('Calculate'):
            compute = ProcessFingerprint(inputdataframe, variance, minmargin,
                                         maxmargin, False, OUTPUTCSVPATH,
                                         OUTPUTJSONPATH)

            with st.spinner('Calculating data...'):
                compute.execute()

            st.success('Done!')
            st.markdown(bin_downloader(OUTPUTJSONPATH, 'processed data'))
