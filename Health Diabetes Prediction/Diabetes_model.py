import joblib
 
def predict(data):
    lr = joblib.load('diabetes_model.joblib')
    return lr.predict(data) 