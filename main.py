import streamlit as st
from dashboard_page import MainPage
from about_page import AboutPage

# App class manages page navigation
class App:
    def __init__(self):
        pass

    def render_pages_template(self):

        mp = MainPage()
        ap = AboutPage()
        
        pg = st.navigation([
            st.Page(mp.dashboard, title='Dashboard'),
            st.Page(ap.about, title='About Page')
        ])
        pg.run()

# Start application
app = App()
app.render_pages_template()