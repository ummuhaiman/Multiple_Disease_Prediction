import streamlit as st
import pickle  

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

def main():
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Check if any input field is empty when the button is clicked
    if st.button('Heart Disease Test Result'):
        input_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        # Check if any input value is empty or whitespace
        if any(value.strip() == '' for value in input_values):
            st.warning('Please fill out all input fields before submitting.')
        else:
            try:
                # Convert input values to float
                user_input = [float(value) for value in input_values]

                # Make prediction
                heart_prediction = heart_disease_model.predict([user_input])

                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is diagnosed with heart disease'
                else:
                    heart_diagnosis = 'The person does not have heart disease'

                st.success(heart_diagnosis)
            
            except ValueError:
                st.error('Invalid input. Please enter numeric values where required.')
    st.markdown("""
        #### Note: 
        
        - chest pain type (0,1,2,3)
        - fasting blood sugar > 120 mg/dl(1=true; 0=false)
        - resting electrocardiographic results (values 0,1,2)
        - exercise induced angina(1=yes,0=no)
        - oldpeak = ST depression induced by exercise relative to rest(0-6.2)
        - the slope of the peak exercise ST segment(0,1,2)
        - number of major vessels (0-3) colored by flourosopy
        - thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
        - sex(1 = male; 0 = female)


    """)

if __name__ == '__main__':
    main()
