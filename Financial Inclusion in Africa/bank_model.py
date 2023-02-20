import joblib
 
def predict(data):
    lr = joblib.load('bank.joblib')
    return lr.predict(data) 