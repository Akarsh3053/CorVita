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


st.title('Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
    trestbps = st.text_input('Resting Blood Pressure')
    restecg = st.text_input('Resting Electrocardiograph results')
    oldpeak = st.text_input('ST depression induced by exercise')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

with col2:
    sex = st.text_input('Sex')
    chol = st.text_input('Serum Cholesterol in mg/dl')
    thalach = st.text_input('Maximum Heart Rate achieved')
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    cp = st.text_input('Chest Pain types')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    exang = st.text_input('Exercise Induced Angina')
    ca = st.text_input('Major vessels colored by fluoroscopy')


heart_diagnosis = ''

if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)
