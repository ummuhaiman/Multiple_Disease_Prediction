import streamlit as st



# Define the main function
def main():
    #st.title("Streamlit Image Click Navigation")

    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    # Display the home page
    if st.session_state.page == 'home':
        #st.header("Home Page")

        # Create two columns
        col1, col2  = st.columns(2,gap='small')

        # Display the first image in the first column
        col1.image("diabetes.jpg", width=250)

        st.markdown(
            """
            <style>
                .stButton > button {
                    width: 250px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display the "Go to Next Page - Image 1" button in the first column
        if col1.button("Diabetes Prediction"):
            st.session_state.page = 'next_page_image1'

        # Display the second image in the second column
        col2.image("heart-man.jpg", width=250)

        # Display the "Go to Next Page - Image 2" button in the second column
        if col2.button("Heart Disease Prediction"):
            st.session_state.page = 'next_page_image2'


       
        # Create two columns for the third image
        col3, col4 = st.columns(2,gap='small')

        # Display the third image in the first column of the second row
        col3.image("parkinsons.jpg", width=250)

        # Display the "Go to Next Page - Image 3" button in the second column of the second row
        if col3.button("Parkinson's Prediction"):
            st.session_state.page = 'next_page_image3'

        col4.image("pnemo.jpg", width=250)

        # Display the "Go to Next Page - Image 4" button in the second column of the second row
        if col4.button("Pneumonia Prediction"):
            st.session_state.page = 'next_page_image4'



        st.markdown("""---""")
        # Add a footer with an FAQ box
        st.markdown(
            """
            ### FAQ

**Q1: How do disease prediction websites work?**

Disease prediction websites use machine learning algorithms to analyze user-provided data, based accurate parameters, to predict potential diseases based on patterns and correlations.

**Q2: Are these predictions accurate?**

Accuracy varies. These websites provide general insights and should not replace professional medical advice. Consultation with a healthcare professional is crucial for accurate diagnosis and treatment.

**Q3: What data is usually required for predictions?**

Typically, these websites ask for information like  medical history, lifestyle factors to generate predictions.

**Q4: Can I trust the privacy of my data on these websites?**

It's essential to review the privacy policy of each website. Reputable platforms prioritize data security and may anonymize or encrypt user information.


**Q5: How often should I use disease prediction websites?**

These tools are not meant for frequent use. If you have persistent health concerns, consult a healthcare professional for a thorough evaluation.

**Q6: Are disease prediction websites a substitute for visiting a doctor?**

No, they are not a substitute. While they can provide insights, a doctor's expertise is crucial for accurate diagnosis, treatment, and personalized care.

**Q7: Can these websites predict rare diseases?**

No,Only diabetes,heart disease,parkinsons,pneumonia.

**Q8: Do disease prediction websites provide emergency assistance?**

No, these websites are not designed for emergencies. In urgent situations, seek immediate medical attention or contact emergency services.

            """
        )

    # Display the next page for Image 1
    elif st.session_state.page == 'next_page_image1':
        st.markdown('<h2 style="color:#800080;">Common Symptoms</h2>', unsafe_allow_html=True)
        st.markdown("""
    - urinate(pee) a lot,often at night
    - Are very thirsty
    - Lose weight without trying
    - Are very hungry
    - Have blurry vision 
    - Have numb or tingling hands or feet
    - Feel very tired
    - Have very dry skin
    - Have sores that heal slowly
    - Have more infections than usual
    """)
        st.markdown('<h2 style="color:#800080;">Types</h2>', unsafe_allow_html=True)
        st.markdown("""
    - Type 1 Diabetes

    People who have type 1 diabetes may also have nausea, vomiting, or stomach pains. Type 1 diabetes can be diagnosed at any age, and symptoms can develop in just a few weeks or months and can be severe.

    - Type 2 Diabetes

    Type 2 diabetes symptoms often take several years to develop. Some people don’t notice any symptoms at all. Type 2 diabetes usually starts when you’re an adult, though more and more children and teens are developing it. Because symptoms are hard to spot, it’s important to know the risk factors for type 2 diabetes. Make sure to visit your doctor if you have any of them

    - Gestational Diabetes

    Gestational diabetes (diabetes during pregnancy) usually doesn’t have any symptoms. If you’re pregnant, your doctor should test you for gestational diabetes between 24 and 28 weeks of pregnancy. If needed, you can make changes to protect your health and your baby’s health.
""")
       

        # Display the "Go back to Home Page" button
        if st.button("Go back to Home"):
            st.session_state.page = 'home'

    # Display the next page for Image 2
    elif st.session_state.page == 'next_page_image2':
        
        st.markdown("""
       
**When to Call the Doctor**

If you have any signs of heart disease, call your health care provider right away. Don't wait to see if the symptoms go away or dismiss them as nothing.

**Call the local emergency number if:**
- You have chest pain or other symptoms of a heart attack
- You know you have angina and have chest pain that doesn't go away after 5 minutes of rest or after taking nitroglycerin
- You think you may be having a heart attack
- You become extremely short of breath
- You think you may have lost consciousness
    """)
        st.markdown('<h2 style="color:#800080;">Common Symptoms</h2>', unsafe_allow_html=True)
        st.markdown("""
    - Chest Pain
    - Shortness of Breath
    - Coughing or Wheezing
    - Swelling in the Legs, Ankles, or Feet
    - Fatigue
    - Fast or Uneven Heartbeat (Palpitations)

    
""")
        st.markdown('<h2 style="color:#800080;">Types Of Heart Diseases</h2>', unsafe_allow_html=True)
        st.markdown("""
    - Coronary artery disease

    Also called: CAD, atherosclerotic heart disease
    Coronary artery disease (CAD) is a narrowing or         blockage of your coronary arteries, which supply oxygen-rich blood to your heart. This happens because, over time, plaque (including cholesterol) buildup in these arteries limits how much blood can reach your heart muscle.


    - Cardiac arrest

    Sudden cardiac arrest (SCA) is the sudden loss of all heart activity due to an irregular heart rhythm. Breathing stops. The person becomes unconscious. Without immediate treatment, sudden cardiac arrest can lead to death.


    - Arrhythmia
    Also called: irregular heartbeat

    A heart arrhythmia (uh-RITH-me-uh) is an irregular heartbeat. A heart arrhythmia occurs when the electrical signals that tell the heart to beat don't work properly. The heart may beat too fast or too slow. Or the pattern of the heartbeat may be inconsistent 
""")
        
        # Display the "Go back to Home Page" button
        if st.button("Go back to Home"):
            st.session_state.page = 'home'

     # Display the next page for Image 3
    elif st.session_state.page == 'next_page_image3':
        st.markdown('<h2 style="color:#800080;">General Information</h2>', unsafe_allow_html=True)
        st.markdown("""
   

Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves.Although Parkinson's disease can't be cured, medications might significantly improve your symptoms. Occasionally, your health care provider may suggest surgery to regulate certain regions of your brain and improve your symptoms.
    """)
        st.markdown('<h2 style="color:#800080;">Common Symptoms</h2>', unsafe_allow_html=True)
        st.markdown("""
    - Tremor: can occur at rest, in the hands, limbs, or can be postural
    - Muscular: stiff muscles, difficulty standing, difficulty walking, difficulty with bodily movements, involuntary movements, muscle rigidity, problems with coordination, rhythmic muscle contractions, slow bodily movement, or slow shuffling gait
    - Sleep: early awakening, nightmares, restless sleep, or sleep disturbances
    - Whole body: fatigue, dizziness, poor balance, or restlessness
    - Cognitive: amnesia, confusion in the evening hours, dementia, or difficulty thinking and understanding
    - Speech: difficulty speaking, soft speech, or voice box spasms
    - Mood: anxiety or apathy
    - Nasal: distorted sense of smell or loss of smell
    - Urinary: dribbling of urine or leaking of urine
    - Facial: jaw stiffness or reduced facial expression
    - Also common: blank stare, constipation, depression, difficulty swallowing, drooling, falling, fear of falling, loss in contrast sensitivity, neck tightness, small handwriting, trembling, unintentional writhing, or weight loss
""")
       

        # Display the "Go back to Home Page" button
        if st.button("Go back to Home"):
            st.session_state.page = 'home'


    # Display the next page for Image 4
    elif st.session_state.page == 'next_page_image4':
        st.markdown('<h2 style="color:#800080;">General Information</h2>', unsafe_allow_html=True)
        st.markdown("""
    

Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.

    """)
        st.markdown('<h2 style="color:#800080;">Common symptoms of pneumonia</h2>', unsafe_allow_html=True)
        st.markdown("""
   

- Persistent cough, which may produce mucus (may be green or yellow)
- Fever, sweating, and chills
- Shortness of breath or difficulty breathing
- Chest pain, especially when breathing or coughing
- Fatigue and weakness
- Loss of appetite
- Bluish lips or nails (in severe cases)
- These symptoms can vary depending on the severity of the infection, the type of pneumonia, and the individual's overall health.
""")
        st.markdown("""
**When to see a doctor**

You should see a doctor if you experience symptoms of pneumonia, such as persistent cough, chest pain, difficulty breathing, fever, or fatigue, especially if these symptoms are severe or worsen over time. Additionally, seek medical attention if you have a weakened immune system, are elderly, or have underlying health conditions, as pneumonia can be more serious in these cases. Early diagnosis and treatment are crucial for managing pneumonia effectively and preventing complications.
""")    

        # Display the "Go back to Home Page" button
        if st.button("Go back to Home"):
            st.session_state.page = 'home'

