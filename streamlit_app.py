"""

Created on Thirsday May 7 13:15:00 2024

@author: Mahesh Solankar

"""
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

pickle_in = open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)

def predict_note_authentication(variance, skewness, curtosis, entropy):
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
    
    prediction=classifier.predict([[
        variance,
        skewness,
        curtosis,
        entropy]]
    )
    return prediction


def main():
    st.title("Bank Authentication")
    html_temp = """
        <div style="background-color:tomato;padding:10x">
        <h2 style=:"color:white; text-align:center;">Streamlit Bank Authentication ML App</h2>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Variance = st.text_input("Variance", "Type Here")
    Skewness = st.text_input("Skewness", "Type Here")
    Curtosis = st.text_input("Curtosis", "Type Here")
    Entropy = st.text_input("Entropy", "Type Here")
    result=""

    if st.button("Predict"):
        result=predict_note_authentication(Variance, Skewness, Curtosis, Entropy)
    st.success("The output is {}".format(result))

    if st.button("About"):
        st.text("Lets Learn")

if __name__== "__main__":
    main()
