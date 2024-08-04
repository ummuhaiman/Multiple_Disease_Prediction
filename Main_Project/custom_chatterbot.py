import streamlit as st
from transformers import BertTokenizer, BertForMaskedLM
import torch
import re
import sqlite3

class CustomChatterBot:
    def __init__(self):
        # Load pre-trained BERT model and tokenizer
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForMaskedLM.from_pretrained('bert-base-uncased')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

        # Connect to the SQLite database
        self.connection = sqlite3.connect('chat_history.db')
        self.create_table()

    def create_table(self):
        # Create a table for chat history if it doesn't exist
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS chat_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender TEXT,
                    message TEXT
                )
            ''')

            # Check if 'sender' and 'message' columns exist, if not add them
            cursor = self.connection.cursor()
            cursor.execute("PRAGMA table_info(chat_history)")
            columns = [col[1] for col in cursor.fetchall()]
            if 'sender' not in columns:
                cursor.execute('''ALTER TABLE chat_history ADD COLUMN sender TEXT''')
            if 'message' not in columns:
                cursor.execute('''ALTER TABLE chat_history ADD COLUMN message TEXT''')

    def get_response(self, user_input):
        # Check for specific patterns in the user input
        if re.search(r'\bpneumonia\b', user_input, re.I):
            return "Pneumonia is an inflammatory condition affecting the lung, primarily caused by infection."
        elif re.search(r'\b(?:cause of|reason for|resons of) diabetes\b', user_input, re.I):
            return "The causes of diabetes vary depending on the type. Type 1 diabetes is often caused by the immune system attacking the insulin-producing cells in the pancreas. Type 2 diabetes is influenced by factors like genetics, lifestyle, and obesity."
        elif re.search(r'\b(?:treat|treatment of) diabetes\b', user_input, re.I):
            return "Diabetes treatment involves lifestyle modifications such as a healthy diet and regular exercise. Medications and insulin therapy may be prescribed based on the individual's needs."
        elif re.search(r'\b(?:676506 pincode nearest|pincode 676506 nearest) hospital\b', user_input, re.I):
            return "MBH Malappuram,kezhakkethala"
        elif re.search(r'\b(?:676505 pincode nearest|pincode 676505 nearest) hospital\b', user_input, re.I):
            return "sahakarana,Malappuram"
        elif re.search(r'\b(?:what is|disease) parkinsons\b', user_input, re.I):
            return " Parkinson’s disease is a condition where a part of your brain deteriorates, causing more severe symptoms over time.While this condition is best known for how it affects muscle control, balance and movement, it can also cause a wide range of other effects on your senses, thinking ability, mental health and more"
        elif re.search(r'\b(?:what is|what is type 2) diabetes\b',user_input,re.I):
            return"Insulin resistance, prediabetes, type 2 diabetes, and type 2 diabetes with vascular complications. You are at higher risk for these conditions if you are older than 45, have close biological relatives with diabetes, are physically inactive, or have extra weight."
        elif re.search(r'\b(?:how does affect|how does affect patient in) diabetes\b',user_input,re.I):
            return"Over time, high blood glucose levels can damage the body's organs. Possible long-term effects include damage to large (macrovascular) and small (microvascular) blood vessels, which can lead to heart attack, stroke, and problems with the kidneys, eyes, gums, feet and nerves."
        elif re.search(r'\b(?:What is the normal sugar|normal sugar) level\b', user_input, re.I):
            return "The expected values for normal fasting blood glucose concentration are between 70 mg/dL (3.9 mmol/L) and 100 mg/dL (5.6 mmol/L). When fasting blood glucose is between 100 to 125 mg/dL (5.6 to 6.9 mmol/L) changes in lifestyle and monitoring glycemia are recommended."
        elif re.search(r'\b(?:What is maximum suger|maximum sugar) level\b', user_input, re.I):
            return "A blood sugar level less than 140 mg/dL (7.8 mmol/L) is normal. A reading of more than 200 mg/dL (11.1 mmol/L) after two hours means you have diabetes. A reading between 140 and 199 mg/dL (7.8 mmol/L and 11.0 mmol/L) means you have prediabetes."
        elif re.search(r'\b(?:What is the final stage of|What is the last stage of) diabetes\b', user_input, re.I):
            return "After many years with diabetes, especially untreated diabetes, a person can develop end stage renal disease or heart disease. Significantly elevated blood sugar levels can lead to diabetic ketoacidosis in people with type 1 diabetes or hyperglycemic hyperosmolar syndrome (HHS) in people with type 2 diabetes."
        elif re.search(r'\b(?:What is the main cause of|cause of) pneumonia\b', user_input, re.I):
            return " Bacteria are a common cause of pneumonia in adults. Many types of bacteria can cause pneumonia, but Streptococcus pneumoniae (also called pneumococcus bacteria) is the most common cause in the United States. Some bacteria causepneumonia with different symptoms or other characteristics than the usual pneumonia. "
        elif re.search(r'\b(?: What are the danger signs of|signs of) pneumonia\b', user_input, re.I):
            return "if you have difficulty breathing, develop a bluish color in your lips and fingertips, have chest pain, a high fever, or a cough with mucus that is severe or is getting worse."
        elif re.search(r'\b(?:What is the best treatment for|treatment for) pneumonia\b', user_input, re.I):
            return " Antibiotics may be prescribed for bacterial pneumonia. Most people begin to feel better after one to three days of antibiotic treatment. However, you should take antibiotics as your doctor prescribes. If you stop too soon, your pneumonia may comeback"
        elif re.search(r'\b(?:How is spread|reasons of spread) pneumonia\b', user_input, re.I):
            return " Pneumonia is mostly spread when people infected cough, sneeze or talk, sending respiratory droplets into the air. These droplets can then be inhaled by close contacts. Less often, you can get pneumonia from touching an object or surface that has the germ on it and then touching your nose or mouth."
        elif re.search(r'\b(?:How can I tell if I have versus the common cold|or the flu) pneumonia\b', user_input, re.I):
            return " It can be difficult to tell the difference between the symptoms of a cold, the flu and pneumonia, and only a healthcare provider can diagnose you. As pneumonia can be life-threatening, it’s important to seek medical attention for serious symptoms that could be signs of pneumonia, such as:Congestion or chest pain,Difficulty breathing,A fever of 102 degrees Fahrenheit (38.88 degrees Celsius) or higher,Coughing up yellow, green or bloody mucus or spit"
        elif re.search(r'\b(?:Who is most at risk of getting|who is most risk of getting) pneumonia\b', user_input, re.I):
            return " You’re at an increased risk of pneumonia if you:Are over the age of 65 and or under the age of 2,Are living with a lung or heart condition,Examples include cystic fibrosis, asthma, chronic obstructive pulmonary disease, emphysema, pulmonary fibrosis or sarcoidosis.Are living with a neurological condition that makes swallowing difficult. Conditions like dementia, Parkinson’s disease and stroke increase your risk of aspiration pneumonia.Are in the hospital or at a long term care facility.Smoke Are pregnant.Have a weakened immunesystem. You might have a weakened immune system if you’re on chemotherapy, are an organtransplant recipient, are living with HIV/AIDS or are taking medications that suppress your immune system"
        elif re.search(r'\b(?:How common is|common is) pneumonia\b', user_input, re.I):
            return " Anyonecangetpneumonia. It’sacommonillness,withmillionsofpeoplediagnosedeachyearintheUnitedStates. About 55,000 people die each year of pneumonia in the U.S. It’s the most common cause of death in developing countries."
        elif re.search(r'\b(?:What are the ways to reduce your risk of|reduce your risk of) pneumonia\b', user_input, re.I):
            return "In addition to getting vaccinated, you can reduce your risk of getting and spreading pneumonia with some healthy habits:-Quit smoking and avoid secondhand smoke. Smoking damages your lungs and makes you more likely to get an infection.-Wash your hands with soap and water before eating, before handling food and after using the restroom. If soap isn’t available, use an alcohol-based hand sanitizer.-Avoid close contact and sharing items with other people if either of you has an infectious disease such as the flu, a cold or COVID-19.-If you have to stay in a hospital or other healthcare facility, don’t be afraid to ask your providers about how to reduce your risk of getting an infection during your stay.-Eat a healthy diet, exercise and get enough rest.-Get treated for any other infections or health conditions you may have. These conditions could weaken your immune system, which could increase your chance of pneumonia.-Avoid excessive alcohol consumption"
        elif re.search(r'\b(?:Who does it affect|who is affect) parkinsons\b', user_input, re.I):
            return " The risk of developing Parkinson’s disease naturally increases with age, and the average age at which it starts is 60 years old. It’s slightly more commoninpeopleassignedmaleatbirth(AMAB)thanpeopleassignedfemaleatbirth(AFAB).while Parkinso’s disease is usually age-related, it can happen in adults as young as 20 (though this is extremely rare, and often people have a parent, full sibling or child with the same condition)."
        elif re.search(r'\b(?:How does this condition affect human body in| How does this condition affect patient in) parkinsons\b', user_input, re.I):
            return " Parkinson’s disease causes a specific area of your brain, the basal ganglia, to deteriorate. As this area deteriorates, you lose the abilities those areas once controlled. Researchers have uncovered that Parkinson’s disease causes a major shift in your brain chemistry.Under normal circumstances, your brain uses chemicals known as neurotransmitters to control how your brain cells(neurons) communicate with each other. When you have Parkinson’s disease, you don’t have enough dopamine, one of the most important neurotransmitters.When your brain sends activation signals that tell your muscles to move, it fine-tunes your movements using cells that require dopamine. That’s why lack of dopamine causes the slowed movements and tremors symptoms of Parkinson’s disease.As Parkinson’s disease progresses, the symptoms expand and intensify. Later stages of the disease often affect how your brain functions, causing dementia-like symptoms and depression"
        elif re.search(r'\b(?:What causes the condition| What reasons the) parkinsons\b', user_input, re.I):
            return " Although there are several recognized risk factors for Parkinson’s disease, such as exposure to pesticides, for now, theonly confirmed causes of Parkinson’s disease are genetic. When Parkinson’s disease isn’t genetic, experts classify it as“idiopathic” (this term comes from Greek and means “a disease of its own”). That means they don’t know exactly why it happens.Many conditions look like Parkinson’s disease but are instead parkinsonism (which refers to Parkinson’s disease-like conditions) from a specific cause like some psychiatric medications.Familial Parkinson’s disease :-Parkinson’s disease can have a familial cause, which means you can inherit it from one or both of your parents. However, this only makes up about 10 Idiopathic Parkinson’s disease :-idiopathic Parkinson’s disease happens because of problems with how your body uses a protein called-synuclein (alpha sy-nu-clee-in). Proteins are chemical molecules that have a very specific shape.When some proteins don’t have the correct shape — a problem known as protein misfolding — your body can’t use themandcan’t break themdown.Withnowheretogo, theproteinsbuild upinvarious places or in certain cells (tangles or clumps of these proteins are called Lewy bodies). The buildup of these Lewy bodies (which doesn’t happen with some of the genetic problems that cause Parkinson’s disease) causes toxic effects and cell damage. Protein misfolding is common in many other disorders, such as Alzheimer’s disease, Huntington’s disease, multiple forms of amyloidosis and more.Induced Parkinsonism :-There are conditions or circumstances experts have linked to parkinsonism. While these aren’t true Parkinson’s disease, they have similar features, and healthcare providers may consider these causes while diagnosing Parkinson’s disease.The possible causes are: The possible causes are:-Medications. Several medications can cause a parkinsonism-like effect. The Parkinson’s-like effects are often temporary if you stop taking the medication that caused them before the effects become permanent. However, the effects can linger for weeks or even months after you stop taking the medication.-Encephalitis. Inflammation of your brain, known as encephalitis, can sometimes cause parkinsonism.-Toxins and poisons. Exposure to several substances, such as manganese dust, carbon monoxide, fumes from welding, or certain pesticides, can lead to parkinsonism.-Damage from injuries. Repeated head injuries, such as those from high-impact or contact sports like boxing, football,hockey, etc., can cause brain damage. The term for this is “post-traumatic parkinsonism."
        elif re.search(r'\b(?:What are the symptoms|symptoms of) parkinsons\b', user_input, re.I):
            return " The best-known symptoms of Parkinson’s disease involve loss of muscle control. However, experts now know that muscle control-related issues aren’t the only possible symptoms of Parkinson’s disease.-Slowed movements (bradykinesia). A Parkinson’s disease diagnosis requires that you have this symptom. People who have this describe it as muscle weakness, but it happens because of muscle control problems, and there’s no actual loss of strength.-Tremor while muscles are at rest. This is a rhythmic shaking of muscles even when you’re not using them and happens in about 80 percentage of Parkinson’s disease cases. Resting tremors are different from essential tremors, which don’t usually happen when muscles are at rest.-Rigidity or stiffness. Lead-pipe rigidity and cogwheel stiffness are common symptoms of Parkinson’s disease. Lead-pipe rigidity is a constant, unchanging stiffness when moving a body part. Cogwheel stiffness happens when you combine tremor and lead-pipe rigidity. It gets its name because of the jerky, stop-and-go appearance of the movements (think of  it as the second hand on a mechanical clock).-Unstable posture or walking gait. The slowed movements and stiffness of Parkinson’s disease cause a hunched over or stooped stance. This usually appears as the disease gets worse. It’s visible when a person walks because they’ll use shorter, shuffling strides and move their arms less. Turning while walking may take several steps.-Blinking less often than usual. This is also a symptom of reduced control of facial muscles.-Cramped or small handwriting. Known as micrographia, this happens because of muscle control problems.-Drooling. Another symptom that happens because of loss of facial muscle control.-Mask-like facial expression. Known as hypomimia, this means facial expressions change very little or not at all.-Trouble swallowing (dysphagia). This happens with reduced throat muscle control. It increases the risk of problems like pneumonia or choking.-Unusually soft speaking voice (hypophonia). This happens because of reduced muscle control in the throat and chest.-Autonomic nervous system symptoms. These include orthostatic hypotension (low blood pressure when standing up),constipation and gastrointestinal problems, urinary incontinence and sexual dysfunctions.-Depression.-Loss of sense of smell (anosmia).-Sleep problems such as periodic limb movement disorder (PLMD), rapid eye movement (REM) behavior disorder and restless legs syndrome.-Trouble thinking and focusing (Parkinson’s-related dementia)"
        elif re.search(r'\b(?:How is it diagnosed|how can diagnosed) parkinsons\b', user_input, re.I):
            return " Diagnosing Parkinson’s disease is mostly a clinical process, meaning it relies heavily on a healthcare provider examining your symptoms, askingyouquestions andreviewing yourmedicalhistory. Some diagnostic and lab tests are possible, but these are usually needed to rule out other conditions or certain causes. However, most lab tests aren’t necessary unless you don’t respond to treatment for Parkinson’s disease, which can indicate you have another condition."
        elif re.search(r'\b(?:How is it treated, and is there a cure|how is cure|what is the treatment) parkinsons\b', user_input, re.I):
            return " For now, Parkinson’s disease is not curable, but there are multiple ways to manage its symptoms. The treatments can also vary from person to person, depending on their specific symptoms and how well certain treatments work. Medications are the primary way to treat this condition.Asecondarytreatmentoptionisasurgerytoimplantadevicethatwilldeliveramildelectricalcurrenttopartofyourbrain(this is known as deep brain stimulation). There are also some experimental options, such as stem cell-based treatments,but their availability often varies, and many aren’t an option for people with Parkinson’s disease."
        elif re.search(r'\b(?:What medications used|medication of) parkinsons\b', user_input, re.I):
            return "Medication treatments for Parkinson’sdisease fall into two categories: Directtreatmentsandsymptomtreatments. Direct treatments target Parkinson’s itself. Symptom treatments only treat certain effects of the disease.Medications-Adding dopamine. Medications like levodopa can increase the available levels of dopamine in your brain. This medication is almost always effective, and when it doesn’t work, that’s usually a sign of some other form of parkinsonism rather than Parkinson’s disease. Long-term use of levodopa eventually leads to side effects that make it less effective.-Simulating dopamine. Dopamine agonists are medications that have a dopamine-like effect. Dopamine is a neurotransmitter, causing cells to act in a certain way when a dopamine molecule latches onto them. Dopamine agonists can latch on and cause cells to behave the same way. These are more common in younger patients to delay starting levodopa.-Dopaminemetabolismblockers. Yourbodyhasnaturalprocessestobreakdownneurotransmitterslikedopamine. Medications that block your body from breaking down dopamine allow more dopamine to remain available to your brain.They’re especially useful early on and can also help when combined with levodopa in later stages of Parkinson’s disease.-Levodopa metabolism inhibitors. These medications slow down how your body processes levodopa, helping it last longer. These medications may need careful use because they can have toxic effects and damage your liver. They’re most often used to help as levodopa becomes less effective. Adenosine blockers. Medications that block how certain cells use adenosine (a molecule used in various forms throughout your body) can have a supportive effect when used alongside levodopa"
        elif re.search(r'\b(?:How can I reduce myrisk or prevent this condition|prevent this condition) parkinsons\b', user_input, re.I):
            return " Parkinson’s disease happens for either genetic reasons or unpredictably. Neither are preventable, and you also can’t reduce your risk of developing it. There are certain high-risk occupations such as farming and welding, but not everyone in these professions develops parkinsonism."
        elif re.search(r'\b(?:How do I take care of myself|take care from) parkinsons\b', user_input, re.I):
            return " If you have Parkinson’s disease, the best thing you can do is follow the guidance of your healthcare provider on how to take care of yourself.-Takeyourmedicationasprescribed. TakingyourmedicationscanmakeahugedifferenceinthesymptomsofParkinson’s disease. You should take your medications as prescribed and talk to your provider if you notice side effects or start to feel like your medications aren’t as effective.-See your provider as recommended. Your healthcare provider will set up a schedule for you to see them. These visits ar especially important to help with managing your conditions and finding the right medications and dosages.-Don’t ignore or avoid symptoms. Parkinson’s disease can cause a wide range of symptoms, many of which are treatable bytreating the conditionorthesymptomsthemselves. Treatment can make a major difference in keeping symptoms from having worse effects"
        elif re.search(r'\b(?:What are the causes of|causes of) heart disease\b', user_input, re.I):
            return "Leading risk factors for heart disease and stroke are high blood pressure, high low-density lipoprotein (LDL) cholesterol, diabetes, smoking and secondhand smoke exposure, obesity, unhealthy diet, and physical inactivity."
        elif re.search(r'\b(?:What causes a weak|reasons of weak) heart\b', user_input, re.I):
            return "The heart muscle can be damaged by certain infections, heavy alcohol use, illegal drug use and some chemotherapy medicines. Your genes also can play a role. Any of the following conditions also can damage or weaken the heart and cause heart failure. Coronary artery disease and heart attack."
        elif re.search(r'\b(?:What is Stage 1 heart failure|Stage 1) heart failure\b', user_input, re.I):
            return "The person has heart disease, but it isn't yet causing symptoms or limiting activities. Stage 2: The person has mild symptoms that only slightly limit activity. Stage 3: The person has significant limitations to activities."
        elif re.search(r'\b(?:Which exercise is good for|exercise is good for) heart\b', user_input, re.I):
            return "Ideally, at least 30 minutes a day, at least five days a week. Examples: Brisk walking, running, swimming, cycling, playing tennis and jumping rope. Heart-pumping aerobic exercise is the kind that doctors have in mind when they recommend at least 150 minutes per week of moderate activity."
        else:
            # Tokenize user input
            input_ids = self.tokenizer.encode(user_input, return_tensors="pt").to(self.device)

            # Mask last token (assuming it's the user's question or incomplete sentence)
            mask_token_index = torch.where(input_ids == self.tokenizer.mask_token_id)[1]
            input_ids[0, mask_token_index] = self.tokenizer.mask_token_id

            # Generate predictions
            with torch.no_grad():
                outputs = self.model(input_ids)
                predictions = outputs.logits

            # Get predicted token IDs
            predicted_token_ids = torch.argmax(predictions[0, mask_token_index], dim=1)

            # Decode predicted token IDs to text
            predicted_tokens = self.tokenizer.convert_ids_to_tokens(predicted_token_ids.tolist())

            # Join tokens to form response
            response = self.tokenizer.convert_tokens_to_string(predicted_tokens)
            return response

    def add_to_history(self, sender, message):
        # Add the message to the chat history and store in the database
        with self.connection:
            self.connection.execute('''
                INSERT INTO chat_history (sender, message) VALUES (?, ?)
            ''', (sender, message))

    def retrieve_chat_history(self):
        # Retrieve chat history from the database
        with self.connection:
            cursor = self.connection.execute('''
                SELECT sender, message FROM chat_history ORDER BY id DESC LIMIT 6
            ''')
            return cursor.fetchall()

    def run(self):
        st.title("Ask Me")

        user_input = st.text_input("You:", "")
        if st.button("Send"):
            if user_input:
                # Get chatbot response
                bot_response = self.get_response(user_input)

                # Add the current conversation to the history and store in the database
                self.add_to_history("You", user_input)
                self.add_to_history("MedicalBot", bot_response)

                # Display user input and bot response
                st.write("You:", user_input)
                st.write("⚕️MedicalBot:", bot_response)

        # Display chat history
        st.subheader("Chat History:")
        for entry in self.retrieve_chat_history():
            st.write(f"{entry[0]}: {entry[1]}")

# Create an instance of the CustomChatterBot class and run the application
custom_chatterbot_app = CustomChatterBot()
custom_chatterbot_app.run()
