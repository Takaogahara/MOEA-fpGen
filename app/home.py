import streamlit as st

def app():
    st.markdown("""## Home""")
    with st.beta_container():
        st.markdown("""### About""")

        st.markdown("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
        labore et dolore magna aliqua. Facilisis leo vel fringilla est ullamcorper eget nulla. 
        Aenean euismod elementum nisi quis eleifend quam. Sed felis eget velit aliquet sagittis id consectetur. 
        Ac odio tempor orci dapibus ultrices in iaculis nunc sed. 
        """)

        st.markdown("""
        **Credits**  
        - App built inspired in [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor)) applications
        - Add more
        """)

    st.markdown("""###""")
    with st.beta_expander('Script explanation'):
        st.markdown("""
        ### Script explanation

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
        labore et dolore magna aliqua. Facilisis leo vel fringilla est ullamcorper eget nulla. 
        Aenean euismod elementum nisi quis eleifend quam. Sed felis eget velit aliquet sagittis id consectetur. 
        Ac odio tempor orci dapibus ultrices in iaculis nunc sed. 
        """)

    st.markdown("""###""")
    with st.beta_expander('Optimizer'):
        st.markdown("""
        ### Optimizer

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
        labore et dolore magna aliqua. Facilisis leo vel fringilla est ullamcorper eget nulla. 
        Aenean euismod elementum nisi quis eleifend quam. Sed felis eget velit aliquet sagittis id consectetur. 
        Ac odio tempor orci dapibus ultrices in iaculis nunc sed. 
        """)

    st.markdown("""#""")
    st.markdown("""#""")
    with st.beta_expander('About the author'):
            st.markdown("""
            Placeholder
            """)