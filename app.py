import json
from flask import Flask, request
from model import get_prediction
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    """ Main page of the app. """
    return "Hello World!"


@app.route('/getPrediction', methods = ['GET', 'POST'])
def getPrediction():
    """ Return JSON serializable output from the model """
    
    model_path = "./models/logistic_fit_SMOTE.pkl"
    sample_df_path  = "./data/sample_df.pkl"
    
    payload = request.get_json()
    print(payload)
    
    age = payload['age']
    workclass = payload['workclass']
    fnlwgt = payload['fnlwgt']
    education = payload['education']
    education_num = payload['education-num']
    marital_status = payload['marital-status']
    occupation = payload['occupation']
    relationship = payload['relationship']
    race  = payload['race']
    sex = payload['sex']
    capital_gain = payload['capital-gain']
    capital_loss = payload['capital-loss']
    hours_per_week= payload['hours-per-week']
    native_country = payload['native-country']
    
    new_obs = pd.DataFrame(data = payload)
    print(new_obs)
    pred = get_prediction(new_obs, model_path, sample_df_path)
    print("---------------------pred----------------")
    print(pred)
    return({'data': [int(pred)] })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
