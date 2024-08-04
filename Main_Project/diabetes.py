import streamlit as st
import pickle  

# Load the diabetes prediction model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

def main():
    # Custom CSS to hide Streamlit menu and footer
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Page title
    st.title('Diabetes Prediction')

    # Input fields for user data
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age of the Person')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    # Button to trigger prediction
    if st.button('Diabetes Test Result'):
        # Check if all input fields are filled
        if (Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age):
            # Make prediction
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
                
            st.success(diab_diagnosis)
        else:
            # Display a warning message if any field is empty
            st.warning('Please fill out all input fields before submitting.')