import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Smoking Prediction App 🚬")

age = st.number_input("Age")
gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])
height = st.number_input("Height (cm)")
weight = st.number_input("Weight")
cigarettes_per_day = st.number_input("Cigarettes per day")

if st.button("Predict"):
    input_data = [age, gender, height, weight, cigarettes_per_day]
    features = pd.DataFrame([input_data], columns=model.feature_names_in_)
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Smoker 🚬")
    else:
        st.success("Non-Smoker 🚭")
