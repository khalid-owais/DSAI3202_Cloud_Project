
import json
import joblib
import numpy as np
import pandas as pd
import os
from azureml.core.model import Model

def init():
    global model
    # Use the name you registered: 'taxi_fare_predictor'
    model_path = Model.get_model_path('taxi_fare_predictor')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        input_df = pd.DataFrame(data)
        prediction = model.predict(input_df)
        return prediction.tolist()
    except Exception as e:
        return str(e)
