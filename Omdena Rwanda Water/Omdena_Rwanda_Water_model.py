import joblib
 
def predict(data):
    lr = joblib.load('https://github.com/Akunnadove/Streamlit-Data-Science-Applications/blob/main/Omdena%20Rwanda%20Water/Omdena_Rwanda_Water_model.joblib')
    return lr.predict(data) 
