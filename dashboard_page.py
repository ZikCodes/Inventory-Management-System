from turtle import onclick
import streamlit as st
import sqlite3
import pandas as pd
import time


# MainPage class controls the dashboard page
class MainPage:
    def __init__(self):
        pass


    # Function that holds the template for our Dashboard components
    def dashboard(self):
        st.set_page_config(page_title='dashboard', initial_sidebar_state='collapsed')

        st.logo('assets\\logo.png', size='large')

        def export_csv():
            conn = get_connection()
            df = pd.read_sql(f'SELECT * FROM inventory', conn)
            csv = df.to_csv(index=False).encode('utf-8')
            conn.close()
            return csv


        # We are creating st.columns to seperate our header from our export button
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
                <h2 style='color: gray; display: inline;'>
                        Dashboard
                        </h2>
                        """, unsafe_allow_html=True)

        with col2:
            #To create space inbetween the header and the export button
            st.space()

        with col3:
           
           st.download_button(
               label='🔻 Export CSV',
               data = export_csv,
               mime='text/csv',
               help='Download Inventory As CSV',
               file_name='inventory.csv'
            )


        st.divider()

        # Creating a connection to our sqlite database that we can call anytime
        def get_connection():
            return sqlite3.connect('inventory.db', check_same_thread=False)
        
        # Creating our database and tables it contains
        def creating_db():
            conn = get_connection()
            cur = conn.cursor()

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT,
                    item_category TEXT,
                    item_quantity INTEGER,
                    low_threshold INTEGER
            )
                """
            )
            conn.commit()
            conn.close()

        # Function We call to add new item to our inventory
        def add_item_to_db(item_name, item_category, item_quantity, low_threshold):
            conn = get_connection()
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO inventory (item_name, item_category, item_quantity, low_threshold) VALUES (?,?,?,?)",
                (item_name, item_category, item_quantity, low_threshold)
            )
            conn.commit()
            conn.close()

        # Fuction We call to remove item from our database inventory
        def delete_item(id):
            conn = get_connection()
            cur = conn.cursor()

            cur.execute(
                "DELETE FROM inventory WHERE id = ?",
                (id,)
            )
            conn.commit()
            conn.close()

        # Function we call to Update the Quantity and Threshold
        def update_item(item_quantity, low_threshold, id):
            conn = get_connection()
            cur = conn.cursor()

            cur.execute(
                "UPDATE inventory SET item_quantity = ?,low_threshold = ?  WHERE id = ?",
                (item_quantity, low_threshold, id)
            )
            conn.commit()
            conn.close()


        # Function to get items from our database
        def fetch_inventory():
            conn = get_connection()
            df = pd.read_sql('SELECT * FROM inventory', conn)
            conn.close()
            return df

        # We call creating_db() Function to Create Our DB and Create Table Called inventory
        creating_db()

        # We assign our fetch_inventory() Function to a variable for easy calls
        inventory = fetch_inventory()

        # Values for our metrics
        total_items = len(inventory)
        total_stocks = inventory['item_quantity'].sum() if not inventory.empty else 0
        low_stocks = inventory[inventory['item_quantity'] <= inventory['low_threshold']]


        # Our Add Button Function
        def add_func():
            @st.dialog('Add New Item')
            def add():
                item_name = st.text_input('Item Name')
                item_category = st.text_input('Item Category')
                item_quantity = st.number_input('Item Quantity',min_value=0, step=1)
                low_threshold = st.number_input('Threshold',min_value=0, step=1)
                if st.button('Submit', width='stretch'):
                    if item_name == "" or item_category == "":
                        st.toast('⚠️ Cannot Submit Empty List!')


                    else:
                        add_item_to_db(item_name, item_category,item_quantity, low_threshold)
                        st.rerun()
                        st.toast('✔️ New Item Successfully Added!')

            add()

        # Our Delete Button Function
        def delete_func():
            if total_items <= 0:
                st.toast('⚠️ No Item In Inventory to Delete!')

            else:
                @st.dialog('Delete Item')
                def delete():
                    if not inventory.empty:
                        selected_id = st.selectbox(
                            'Select Item ID',
                            inventory['id'])
                        
                        if st.button('Delete', width='stretch'):
                            delete_item(selected_id)
                            st.rerun()
                            st.toast('✔️ Item Successfully Deleted!')
                            
                delete()

        # Our Update Button Function
        def update_func():
            if total_items <=0 :
                st.toast('⚠️ No Item To Update!')

            else:
                @st.dialog('Update Item')
                def update():
                    if not inventory.empty:
                        selected_id = st.selectbox(
                            'Seleect Item ID',
                            inventory['id']
                        )

                        item_quantity = st.number_input('New Quantity', min_value=0, step=1)
                        low_threshold = st.number_input('New Threshold', min_value=0, step=1)
                        if st.button('Submit', width='stretch'):
                            update_item(item_quantity, low_threshold, selected_id)
                            st.rerun()
                            st.toast('✔️ Successfully Updated!')

                update()
        
        # We create an st.container to display our metrics
        with st.container(border=True):
            st.subheader('Inventory Metrics')
            
            # We create 3 st.columns to seperate our metrics to be side by side
            col1, col2, col3 = st.columns(3)
            
            # Column 1 displays the total items
            with col1:
                st.metric('Total Items', value=f'{total_items}')

            # Column 2 displays the total stocks
            with col2:
                st.metric('Total Stocks', value=f'{total_stocks}')

            # Column 3 displays the low stocks
            with col3:
                st.metric('Low Stocks', value=len(low_stocks))

        
        # Creating a frame for displaying our action Buttons (Add, Delete, Update)
        with st.container(border=True):
            st.subheader('Action Menu')
            col1, col2, col3 = st.columns(3)
            with col1:
                st.button('Add Item', width=150, on_click=add_func) #add_func is the function at line 115

            with col2:
                st.button('Delete Item', width=150, on_click=delete_func) #delete_func is the function at line 135

            with col3:
                st.button('Update', width=150, on_click=update_func) #update_func is the function at line 155

        # Creating a dataframe to display low stock items
        if not low_stocks.empty:
            st.warning('⚠️ Low Stock Alert!')
            st.dataframe(low_stocks[['item_name','item_quantity','low_threshold']], use_container_width=True)
        
        # Creating a dataframe to display all items in our inventory
        with st.container(border=True):
            st.subheader('Inventory')
            st.dataframe(inventory, use_container_width=True)
            if total_items <= 0:
                st.warning('⚠️ No Item In Inventory!')
