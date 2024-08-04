import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from about import main as about_content
#from chatbot import main as chatbot_content
from custom_chatterbot import CustomChatterBot
from account import display_app
from new_home import main as home_content


# Load your company logo
company_logo = Image.open("medical_new.png")



with st.sidebar:
    # Add space at the top for a cleaner layout
    st.markdown("#")

    # Display company logo and name
    st.image(company_logo, width=200)

    # Center-align the title
    st.markdown("<h1 style='text-align: center; color: #333;'>Health Cure</h1>", unsafe_allow_html=True)
    st.markdown("""---""")
    # Create a sidebar option menu
    selected_page = option_menu('Main Menu',
                                ['Home','Account', 'About', 'Chatbot'],
                                icons=['house', 'person', 'kanban'],
                                default_index=0,
                                styles={"nav-link-selected": {"background-color": "#90EE90", "color": "#333"}})

# Content based on the selected page
if selected_page == "Home":
    
   
    #st.set_page_config(layout="wide")
    home_content()
    # Call the main function from the home module
    #st.title("Home Page")

elif selected_page == "Account":
    # Apply centered layout using custom CSS
    
    display_app()

    #st.title("Account Page")

elif selected_page == "About":
    about_content()
    # Add content for the about page
    #st.title("About Page")

#elif selected_page == "Chatbot":
    #chatbot_content()
    # Add content for the chatbot page
    #st.title("Chatbot Page")

elif selected_page == "Chatbot":
    # Create an instance of CustomChatterBot and run it
    custom_chatterbot_app = CustomChatterBot()
    custom_chatterbot_app.run()
