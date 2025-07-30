import streamlit as st
import pandas as pd
import pickle

# Load model and feature columns
model = pickle.load(open("model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("House Price Predictor")

# Old Inputs
area = st.number_input("Area Size (Marla/Kanal)", 1.0, 100.0)
baths = st.slider("Number of Bathrooms", 1, 10)
beds = st.slider("Number of Bedrooms", 1, 10)
is_dha = st.checkbox("Located in DHA?")

# New Inputs
floors = st.slider("Number of Floors", 1, 5)
garage = st.checkbox("Has Garage?")
year_built = st.number_input("Year Built", 1950, 2025)

# Combine inputs
input_data = pd.DataFrame([{
    'Area Size': area,
    'baths': baths,
    'bedrooms': beds,
    'is_DHA': 1 if is_dha else 0,
    'floors': floors,
    'garage': 1 if garage else 0,
    'year_built': year_built
}])

# Fill missing columns with 0
for col in model_columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Reorder to match training
input_data = input_data[model_columns]

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Price: Rs {int(prediction[0]):,}")
