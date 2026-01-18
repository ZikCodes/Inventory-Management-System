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
                time.sleep(0.1)

        # Container to display animated project description
        with st.container(border=True):
            st.write_stream(stream_data)

        # Function to display group members one at a time
        def group_members():
            name_list: list[str] = ['Achor Dorcas Ojone (Leader)','Mohammed Abubakar Sadiku (Member)','Usman Mansur Usman (Member)','Stephen Barnabas (Member)','Bakare Muhammed Bashir (Member)','Abdurrazak Muktar (Member)']
            for i in name_list:
                yield f'{i}\n\n'
                time.sleep(0.8)

        # Container for group members section
        with st.container(border=True, gap='small'):
            st.subheader('Group7 Members', text_alignment='center')
            st.divider()
            col1, col2, col3 = st.columns(3)
            with col1:
                st.space()

            with col2:
                st.write_stream(group_members)
            
            with col3:
                st.space()
