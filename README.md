
# Inventory Management System  


## 1. Project Introduction

    The Inventory Management System is a Python-based web application developed using Python, Streamlit and SQLite.  

    This project allows users to:
        Add new inventory items
        Update item quantities and thresholds
        Delete inventory records
        View inventory statistics
        Export inventory data for reporting


## 2. Technologies Used

    Python
    Pandas - To read our database into a dataframe and also to be able to turn our database table into a CSV
    Streamlit - Web Framework
    Sqlite3 - Our Local Database

## 3. Project Structure

    └── .venv  -> (Our Virtual environment)
    └── main.py
    └── dashboard_page.py
    └── about_page.py
    └── inventory.db
    └── assets
        └── logo.png
    └── README.md


### 4 - Project Structure Diagram

![Project Structure Diagram]('assets/project_structure.png')


### 4.1 main.py – Application Entry Point

This file is the starting point of the application.

    1. Handles navigation between pages
    2. Connects all components together
    3. Runs the Streamlit application


### 4.2 dashboard_page.py – Dashboard and Database Logic

This file contains the main functionality of the application.

#### Key Responsibilities:
    Database creation and connection
    Adding, updating, deleting inventory items
    Displaying inventory metrics
    Exporting inventory data to CSV

##### Database Table:
    Automatically created if it does not exist
    Stores item name, category, quantity, and threshold

##### Dashboard Features:
    Inventory metrics
    Action buttons (Add, Delete, Update)
    Low-stock alerts
    Data table display


### 4.3 about_page.py – About Page
This file displays:
    Project description
    Group members
    Logo and visual layout

Note: It does not use or interact with our database.


## 5. How to Run the Project

### Step 1: Install Dependencies

pip install streamlit pandas


### Step 2: Run the App

streamlit run main.py


## 6. Database Design

Column - Description 

    id - Unique item ID
    item_name - Name of item
    item_category - Item category
    item_quantity - Quantity available
    low_threshold - Minimum stock limit


