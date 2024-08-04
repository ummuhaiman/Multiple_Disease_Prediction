import streamlit as st
from streamlit_lottie import st_lottie
import json
import sqlite3
from heart import main as heart_content
from diabetes import main as diabetes_content
from parkinsons import main as parkinsons_content
from pneumonia import main as pneumonia_content
from streamlit_option_menu import option_menu

# Function to load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Function to create the SQLite database and users table
def create_users_table():
    # Connect to SQLite database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()

    # Create users table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    email TEXT UNIQUE,
                    password TEXT,
                    username TEXT
                 )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to authenticate user
def authenticate_user(email, password):
    # Connect to SQLite database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()

    # Check if user exists with provided credentials
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()

    # Close database connection
    conn.close()

    return user

# Function to create user account
def create_account(email, password, username):
    # Connect to SQLite database
    conn = sqlite3.connect('user.db')
    c = conn.cursor()

    # Insert user into the database
    c.execute("INSERT INTO users (email, password, username) VALUES (?, ?, ?)", (email, password, username))
    conn.commit()

    # Close database connection
    conn.close()

# Function to display login/signup form
def display_app():
    # Create users table if it doesn't exist
    create_users_table()

    # Check if user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        # Load Lottie animation
        lottie_coding = load_lottiefile("Animation.json")  # replace link to local lottie file
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=None,
            width=None,
            key=None,
        )

        # Display welcome message
        st.write("<div class='sub'>Welcome to the Health Cure!</div>", unsafe_allow_html=True)

        # Add some vertical spacing for a cleaner look
        st.write("")
        st.write("")

        # Create a centered login form
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        if choice == 'Login':
            if st.button('Login'):
                user = authenticate_user(email, password)
                if user:
                    st.session_state.logged_in = True
                    st.write("<p style='color: green;'>Login successful</p>",unsafe_allow_html=True)
        else:
            username = st.text_input('Enter Your unique username')
            if st.button('Create My Account'):
                create_account(email, password, username)
                #st.write("Account created successfully. Please login.")
                st.write("<p style='color: green;'>Account created successfully. Please login.</p>", unsafe_allow_html=True)
    else:
        # Logout button
        if st.button('Logout'):
            st.session_state.logged_in = False

        # Display disease prediction options without sidebar
        selected_page = st.selectbox('Disease Prediction', ['Diabetes', 'Heart Disease', 'Parkinsons Disease', 'Pneumonia'])
        if selected_page == "Diabetes":
            diabetes_content()  # Call the main function from the diabetes module

        elif selected_page == "Heart Disease":
            heart_content()

        elif selected_page == "Parkinsons Disease":
            parkinsons_content()

        elif selected_page == "Pneumonia":
            pneumonia_content()

# Main function
if __name__ == "__main__":
    display_app()
