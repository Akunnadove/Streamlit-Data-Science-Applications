import joblib
import numpy as np
import streamlit as st
from PIL import Image


# from Omdena_Rwanda_Water_model import predict

def predict(data):
    lr = joblib.load('Omdena_Rwanda_Water_model.joblib')
    return lr.predict(data)


pics = Image.open("Blue.jpg")

# page_image = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("data:image/png;base64,{pics}");
# background-size: 200%;
# background-position: top left;
# background-repeat: no-repeat;
# background-attachment: local;
# }}
# </style>
# """

# st.markdown(page_image, unsafe_allow_html=True)
st.image(pics)

st.sidebar.header("PREDICTION DASHBOARD")

st.markdown(
    """
    <h1>OMDENA WATER QUALITY PREDICTION PROJECT</h1>
    <br>
    WELCOME TO THIS APPLICATION DESIGNED TO FORECAST WATER POTABILITY USING PROVIDED INPUTS
    <hr>    
    """, unsafe_allow_html=True)

# Colour (TCU)
Colour = st.number_input(label="Colour (TCU)", min_value=0, max_value=1000, format="%d")

# Turbidity (NTU)
Turbidity = st.number_input(label="Turbidity (NTU)", min_value=0, max_value=1000, format="%d")

# pH
pH = st.number_input(label="pH", min_value=0, max_value=1000, format="%d")

# Conductivity (uS/cm)
Conductivity = st.number_input(label="Conductivity (uS/cm)", min_value=0, max_value=1000, format="%d")

# Total Dissolved Solids (mg/l)
TotalDissolvedSolids = st.number_input(label="Total Dissolved Solids (mg/l)", min_value=0, max_value=1000, format="%d")

# Total Hardness (mg/l as CaCO3)
TotalHardness = st.number_input(label="Total Hardness (mg/l as CaCO3)", min_value=0, max_value=1000, format="%d")

# Aluminium (mg/l)
Aluminium = st.number_input(label="Aluminium (mg/l)", min_value=0, max_value=1000, format="%d")

# Chloride (mg/l)
Chloride = st.number_input(label="Chloride (mg/l)", min_value=0, max_value=1000, format="%d")

# Total Iron (mg/l)
TotalIron = st.number_input(label="Total Iron (mg/l)", min_value=0, max_value=1000, format="%d")

# Sodium (mg/l)
Sodium = st.number_input(label="Sodium (mg/l)", min_value=0, max_value=1000, format="%d")

# Sulphate (mg/l)
Sulphate = st.number_input(label="Sulphate (mg/l)", min_value=0, max_value=1000, format="%d")

# Zinc (mg/l)
Zinc = st.number_input(label="Zinc (mg/l)", min_value=0, max_value=1000, format="%d")

# Magnesium (mg/l)
Magnesium = st.number_input(label="Magnesium (mg/l)", min_value=0, max_value=1000, format="%d")

# Calcium (mg/l)
Calcium = st.number_input(label="Calcium (mg/l)", min_value=0, max_value=1000, format="%d")

# Potassium (mg/l)
Potassium = st.number_input(label="Potassium (mg/l)", min_value=0, max_value=1000, format="%d")

# Nitrate (mg/l)
Nitrate = st.number_input(label="Nitrate (mg/l)", min_value=0, max_value=1000, format="%d")

# Phosphate (mg/l)
Phosphate = st.number_input(label="Phosphate (mg/l)", min_value=0, max_value=1000, format="%d")

cost = predict(np.array([[Colour, Turbidity, pH, Conductivity, TotalDissolvedSolids, TotalHardness, Aluminium,
                          Chloride, TotalIron, Sodium, Sulphate, Zinc, Magnesium, Calcium, Potassium, Nitrate,
                          Phosphate]]))

val = cost[0]

if st.button('Check Status'):
    if val == 0:
        st.success("Water is Potable")
    else:
        st.error("Water is Not Potable")
