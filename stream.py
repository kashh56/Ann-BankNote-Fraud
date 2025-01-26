import streamlit as st
import pickle
import numpy as np

# Load the saved model and scaler using pickle
with open('best_model.pkl', 'rb') as model_file:
    best_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit User Interface

# Title of the app
st.title("Banknote Authentication Prediction")

# Define the input fields for the user to fill in
variance = st.number_input("Variance", min_value=-20.0, max_value=20.0, value=0.0)
skewness = st.number_input("Skewness", min_value=-20.0, max_value=20.0, value=0.0)
curtosis = st.number_input("Curtosis", min_value=-20.0, max_value=20.0, value=0.0)
entropy = st.number_input("Entropy", min_value=-20.0, max_value=20.0, value=0.0)

# Collect the inputs into a list
input_data = [variance, skewness, curtosis, entropy]

# When the user clicks the "Predict" button
if st.button("Predict"):
    # Scale the input data using the same scaler used during training
    input_data_scaled = scaler.transform([input_data])

    # Make the prediction using the loaded model
    prediction = best_model.predict(input_data_scaled)

    # Display the result based on the model's prediction
    if prediction > 0.5:
        st.write("The banknote is **genuine** (prediction: 1).")
    else:
        st.write("The banknote is **forged** (prediction: 0).")
