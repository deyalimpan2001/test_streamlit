import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height (in meters):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")