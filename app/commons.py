import streamlit as st
import base64
import os


def bin_downloader(file_path, download_name='file'):
    """
    Create binaries to download.

    Parameters
    ----------
    file_path: str
        File path to be downloaded

    download_name: str
        Default value = 'File'
        Output name of the file

    Returns
    -------
    base64
        File to be downloaded
    """

    if (file_path is not None) and isinstance(file_path, str):
        with open(file_path, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(file_path)}">Download {download_name}</a>'

        return href


class Sidebar():

    def sidebar_uploader(text: str, extension: str, **kwargs):
        """
        Create streamlit upload sidebar

        Parameters
        ----------
        text: str
            Text to be displayed

        extension: str
            Target file extension

        kwargs['file_path']: str
            Path to the example file to be downloaded

        kwargs['exemple_text']: str
            Exemple test to be displayed

        Returns
        -------
        upload_file
            Uploaded file
        """
        upload_file = st.sidebar.file_uploader(text, type=[extension])

        if len(kwargs) > 0:
            st.sidebar.markdown(bin_downloader(kwargs['file_path'],
                                               kwargs['exemple_text']),
                                unsafe_allow_html=True)

        return upload_file

    def sidebar_dict_select(select_dict: dict, text: str):
        """
        Create streamlit dropdown menu sidebar

        Parameters
        ----------
        select_dict: dict
            Dictionary containing the options

        text: str
            Text to be displayed

        Returns
        -------
        selected_item
            str
        """
        options = st.sidebar.selectbox(text, list(select_dict.keys()))
        selected_item = select_dict[options]

        return selected_item
