"""
Created on Tuesday March 05 13:30:00 2024 

@author: Mahesh Solankar
"""
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict', methods=['GET'])
def predict_note_authentication():
    """Let's Authenticate the Bank Note
    This is using dockstring for specification.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    response:
        200:
            description: The output values
    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    
    prediction=classifier.predict([[
        variance,
        skewness,
        curtosis,
        entropy]]
    )
    return "Predicted value is : " + str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Bank Note
    This is using dockstring for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    response:
        200:
            description: The output value
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "Predicted value for the csv is : " + str(prediction)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", use_reloader=False)