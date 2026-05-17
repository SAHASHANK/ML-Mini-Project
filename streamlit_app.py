
import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("random_forest_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]

# Page settings
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.title("House Price Predictor")
st.write("Enter property details to estimate the house price in Indian Rupees.")

# Inputs
area = st.number_input("Total Area (sq ft)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
floors = st.number_input("Floors", min_value=1, step=1)
year_built = st.number_input("Year Built", min_value=1900, max_value=2100, step=1)

location = st.selectbox("Location", ["Downtown", "Suburban", "Rural"])
condition = st.selectbox("Condition", ["Excellent", "Good", "Fair"])
garage = st.selectbox("Garage", ["Yes", "No"])

# Prediction
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "YearBuilt": year_built,
        "Location": location,
        "Condition": condition,
        "Garage": garage
    }])

    prediction = model.predict(input_df)[0]


import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("random_forest_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]

# Page settings
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.title("House Price Predictor")
st.write("Enter property details to estimate the house price in Indian Rupees.")

# Inputs
area = st.number_input("Total Area (sq ft)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
floors = st.number_input("Floors", min_value=1, step=1)
year_built = st.number_input("Year Built", min_value=1900, max_value=2100, step=1)

location = st.selectbox("Location", ["Downtown", "Suburban", "Rural"])
condition = st.selectbox("Condition", ["Excellent", "Good", "Fair"])
garage = st.selectbox("Garage", ["Yes", "No"])

# Prediction
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "YearBuilt": year_built,
        "Location": location,
        "Condition": condition,
        "Garage": garage
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated House Price: ₹{prediction:,.2f}")
