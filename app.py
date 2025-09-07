import numpy as np
import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Crop Prediction Model 🌾")

# Input fields
Nitrogen = st.text_input("Nitrogen")
Phosphorus = st.text_input("Phosphorus")
Potassium = st.text_input("Potassium")
temperature = st.text_input("Temperature")
humidity = st.text_input("Humidity")
ph = st.text_input("pH")
rainfall = st.text_input("Rainfall")

if st.button("Predict"):
    try:
        float_features = [
            float(Nitrogen),
            float(Phosphorus),
            float(Potassium),
            float(temperature),
            float(humidity),
            float(ph),
            float(rainfall)
        ]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        st.success(f"The Predicted Crop is: {prediction[0]}")
    except Exception as e:
        st.error("Please enter valid numbers for all fields.")