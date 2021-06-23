import streamlit as st


def app():
    st.markdown("""## Home""")
    with st.beta_container():
        st.markdown("""### About""")

        st.markdown("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        labore et dolore magna aliqua. Facilisis leo vel fringill
        Aenean euismod elementum nisi quis eleifend quam. Sed fel
        Ac odio tempor orci dapibus ultrices in iaculis nunc sed.
        """)

        st.markdown("""
        **Credits**
        - App built inspired in [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor)) applications
        - Add more
        """)

    st.markdown("""###""")
    with st.beta_expander('Data Extractor'):
        st.markdown("""
        ### Data Extractor explanation:

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, se
        labore et dolore magna aliqua. Facilisis leo vel fringilla
        Aenean euismod elementum nisi quis eleifend quam. Sed felis
        Ac odio tempor orci dapibus ultrices in iaculis nunc sed.

        - Variance threshold value:
        Features with a variance lower than this threshold will be removed.

        - Min/Max search tolerance:
        Minimum and maximum margin tolerance
        """)

    st.markdown("""###""")
    with st.beta_expander('Generator'):
        st.markdown("""
        ### Generator explanation:

        Lorem ipsum dolor sit amet, consectetur adipiscin
        labore et dolore magna aliqua. Facilisis leo vel
        Aenean euismod elementum nisi quis eleifend quam.
        Ac odio tempor orci dapibus ultrices in iaculis n

        - Fixed mean optimization:
        Fixed mean optimization don't change the distance using a random float number

        - Variable mean optimization:
        Variable mean optimization changes the distance using a random float number
        """)

    st.markdown("""#""")
    st.markdown("""#""")
    with st.beta_expander('About the author'):
        st.markdown("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            labore et dolore magna aliqua. Facilisis leo vel fringill
            Aenean euismod elementum nisi quis eleifend quam. Sed fel
            Ac odio tempor orci dapibus ultrices in iaculis nunc sed
            """)
