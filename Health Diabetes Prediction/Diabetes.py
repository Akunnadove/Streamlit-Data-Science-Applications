#Import Python Libraries
import numpy as np
import streamlit as st
from Diabetes_model import predict

with open("C:/Users/Akunna Anyamkpa/diabetes.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.header("Health Analytics")

with st.container():
    st.title('Diabetes Prediction Project')

    st.markdown(
    "Welcome to this application which predicts a patient status as being likely diabetic or not")

st.write('---')

# Patient Pregnancies
Pregnancies = st.number_input('Pregnancies', min_value=0, step=1)
 
# Patient Glucose
Glucose = st.slider('Glucose', 0, 199, 250)
 
# Patient Blood Pressure
BloodPressure = st.slider('Blood Pressure', 0, 122, 150)

# Patient Skin Thickness
SkinThickness = st.slider('Skin Thickness', 0, 50, 120)

# Patient Insulin
Insulin = st.slider('Insulin', 0, 1000)
 
# Patient Body Mass Index
BMI = st.number_input('Body Mass Index', min_value=0, step=1)
 
# Patient Diabetes Pedigree Function
DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function', 0, 3)
 
# Patient Age
Age = st.number_input('Age', min_value=0, step=1)

 
if st.button('Check Status'):
    cost = predict(np.array([[Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]))
    
    val = cost[0]
    
    if val == 0:
        st.text("Patient is not diabetic")
    else:
        st.text("Patient is likely diabetic") 