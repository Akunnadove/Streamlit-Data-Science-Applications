import numpy as np
import streamlit as st
from bank_model import predict

st.sidebar.header("PUBLIC DASHBOARD")

with st.container():
    st.title('Financial Inclusion in Africa')
    st.markdown('Welcome to this application which predicts if a user has a bank account or not')

st.write('---')

st.subheader('Select the appropriate option that applies to you')

# country
country = st.selectbox('Country', ('Kenya','Rwanda','Tanzania','Uganda'))
st.write('You selected =',country)
if country == 'Kenya':
    country = 0
elif country == 'Rwanda':
    country = 1
elif country == 'Tanzania':
    country = 2
elif country == 'Uganda':
    country = 3

# year
year = st.slider('year',2016 , 2017, 2018)

# location_type
location_type = st.radio("Location type", ('Urban','Rural'))
st.write('Your favorite color is',location_type)
if location_type == 'Urban':
    location_type = 0
elif location_type == 'Rural':
    location_type = 1
     
# cellphone_access
cellphone_access = st.selectbox('cellphone access', ('Yes','No'))
if cellphone_access == 'Yes':
    cellphone_access = 0
elif cellphone_access == 'No':
    cellphone_access = 1    
    
# household_size
household_size = st.number_input('household_size', min_value=0, step=1)
    
# age_of_respondent
age_of_respondent = st.number_input('age_of_respondent', min_value=0, step=1)
 
    
# gender_of_respondent
gender_of_respondent = st.selectbox('gender_of_respondent', ('Female','Male'))
if gender_of_respondent == 'Female':
    gender_of_respondent = 0
elif gender_of_respondent == 'Male':
    gender_of_respondent = 1
    
    
# relationship_with_head
relationship_with_head = st.selectbox('relationship_with_head', ('Child','Head of Household','Other non-relatives','Other relative','Parent','Spouse'))
if relationship_with_head == 'Child':
    relationship_with_head = 0
elif relationship_with_head == 'Head of Household':
    relationship_with_head = 1
elif relationship_with_head == 'Other non-relatives':
    relationship_with_head = 2
elif relationship_with_head == 'Other relative':
    relationship_with_head = 3
elif relationship_with_head == 'Parent':
    relationship_with_head = 4
elif relationship_with_head == 'Spouse':
    relationship_with_head = 5
    
    
# marital_status
marital_status = st.selectbox('marital_status', ('Divorced/Seperated','Dont know','Married/Living together','Single/Never Married','Widowed'))
if marital_status == 'Divorced/Seperated':
    marital_status = 0
elif marital_status == 'Dont know':
    marital_status = 1
elif marital_status == 'Married/Living together':
    marital_status = 2
elif marital_status == 'Single/Never Married':
    marital_status = 3
elif marital_status == 'Widowed':
    marital_status = 4
    
    
# education_level
education_level = st.selectbox('education_level', ('No formal education','Other/Dont know/RTA','Primary education','Secondary education','Tertiary education','Vocational/Specialised training'))
if education_level == 'No formal education':
    education_level = 0
elif education_level == 'Other/Dont know/RTA':
    education_level = 1
elif education_level == 'Primary education':
    education_level = 2
elif education_level == 'Secondary education':
    education_level = 3
elif education_level == 'Tertiary education':
    education_level = 4
elif education_level == 'Vocational/Specialised training':
    education_level = 5
    
# job_type
job_type = st.number_input('job_type', min_value=0, step=1)

st.write('You selected =',cellphone_access,education_level) 

if st.button('Check Status'):
    with st.spinner('Model working....'):
        bank_account = predict(np.array([[country, year, location_type, cellphone_access, household_size, age_of_respondent,             gender_of_respondent, relationship_with_head, marital_status, education_level, job_type]]))
        st.success('Processed')
        val = bank_account[0]
        if val == 0:
            st.text("User Does Not Have A Bank Account")
        else:
            st.text("User Has A Bank Account") 
        