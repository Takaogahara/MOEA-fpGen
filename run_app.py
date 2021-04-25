import streamlit as st
from app import home, main_optmizer, main_extract

class MultiApp:
    '''Framework for combining multiple streamlit applications.'''
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
                'title': title,
                'function': func})

    def run(self):
        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()

if __name__ == '__main__':
    app = MultiApp()

    st.markdown("""# Titulo""")

    app.add_app('Home', home.app)
    app.add_app('Data extractor', main_extract.app)
    app.add_app('Generator', main_optmizer.app)

    app.run()