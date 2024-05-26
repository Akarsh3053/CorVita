import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide")

# loading the saved model

heart_disease_model = pickle.load(open('model/heart_disease_model.sav', 'rb'))

page = option_menu(
    menu_title="Heart Disease Prediction",
    options=["Home", "Prediction", "Suggestions"],
    icons=["house-heart-fill", "clipboard2-pulse-fill", "postcard-heart-fill"],
    menu_icon="heart-pulse",
    orientation="horizontal")

if page == "Home":
    body = """
        <h2>Heart Disease Scenario</h2>
        <p>Lack of awareness about heart diseases is a significant concern that contributes to increased mortality risk globally.
        Many people are uninformed about the symptoms, risk factors, and preventive measures associated with heart conditions.
        This lack of knowledge often leads to delayed or avoided medical care, allowing the disease to progress unchecked.
        Additionally, misconceptions about heart diseases being 'old-age' ailments can result in younger individuals neglecting 
        their cardiovascular health. Increased efforts towards public education, early detection, and lifestyle modifications can 
        significantly reduce the mortality risk associated with heart diseases.</p>
        <h3>How this app helps ?</h3>
        <p>An app-based solution that can track, predict, and provide insights on heart health has the potential to revolutionize cardiovascular care and significantly reduce mortality rates. By leveraging advanced technologies like AI and machine learning, these apps can analyze user data, such as heart rate, blood pressure, and lifestyle habits, to identify potential risks and predict heart diseases at an early stage. Moreover, they can offer personalized recommendations for diet, exercise, and stress management, empowering individuals to take control of their heart health. With real-time monitoring and timely alerts, these apps can ensure prompt medical intervention when needed. By making heart health management more accessible, convenient, and proactive, app-based solutions can indeed change the picture for the better.</p>
        """
    la1, la2 = st.columns(2)
    with la1:
        st.image("assets/heart.jpg")
    with la2:
        st.markdown(body, unsafe_allow_html=True)
    st.markdown("<hr style='border:1px dashed #FF4B4B'>",
                unsafe_allow_html=True)

if page == "Prediction":
    st.subheader("Patient details :")

    x,y = st.columns(2)

    with x:
        name = st.text_input('Your name ?')
        sex = st.radio('Sex', ['Male', 'Female'])
        sex = 0 if sex == 'Male' else 1
    
    with y:
        age = str(st.number_input('Age',10,95))
        diabetic = st.radio('Diabetic', ['Yes', 'No'])
        diabetic = 0 if diabetic == 'No' else 1

    st.subheader("Diagnosis parameters from reports:")
    col1, col2, col3 = st.columns(3)
    with col1:

        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiograph results')
        oldpeak = st.text_input('ST depression induced by exercise')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    with col2:
        cp = st.text_input('Chest Pain types')
        chol = st.text_input('Serum Cholesterol in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('Major vessels colored by fluoroscopy')


    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.success(heart_diagnosis)
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)
