import streamlit as st
import time

# AboutPage class handles everything shown on the About page
class AboutPage:
    def __init__(self):
        pass

    # This function renders the About page UI
    def about(self):
        # Display application logo
        st.logo('assets\\logo.png', size='large')

        # Page header
        st.header('About Project', text_alignment='center')
        st.divider()


        # Function to stream text word-by-word for animation effect
        def stream_data():
        
            words = "This software allows you to manage your inventory database with ease. You can add new items, update existing records, delete entries, and export your data to CSV for reporting or backup purposes. It provides a straightforward way to keep your inventory organized and up to date."

            for word in words.split(" "):
                yield word + " "
                time.sleep(0.11)

        # Container to display animated project description
        with st.container(border=True):
            st.write_stream(stream_data)

        with st.container(border=False, height=180):
            pass

        with st.container(border=False):
            col1, col2, col3 =st.columns(3)
            with col1:
                st.space()

            with col2:
                st.space()

            with col3:
                st.markdown("""
                    <h6 style='color: red;text-decoration: underline;'>
                            Created By Zik
                            </h2>
                """, unsafe_allow_html=True)
        
