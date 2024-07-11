import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height * height)

def interpret_bmi(bmi):

  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal weight"
  elif bmi <= 29.9:
    return "Overweight"
  else:
    return "Obese"

st.title("BMI Calculator")
st.markdown("**Created by:** Mohammad Arshan Shaikh")


weight = st.slider("Enter your weight (kg):", min_value=0.0, max_value=200.0, step=0.1)
height = st.slider("Enter your height (m):", min_value=0.0, max_value=2.5, step=0.01)

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

st.write(f"Your BMI is: {bmi:.2f}")
st.write(f"BMI Category: {category}")


