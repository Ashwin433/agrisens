import streamlit as st
import numpy as np
import pickle

# Load trained model and encoder
model = pickle.load(open("RF.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

# Streamlit UI
st.set_page_config(page_title="Crop Recommendation System", page_icon="🌾", layout="centered")

# Custom CSS to hide Streamlit footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# App Title
st.title("🌾 Smart Crop Recommendation System")

# Input fields
col1, col2 = st.columns(2)

with col1:
    nitrogen = st.number_input("Nitrogen (N)", min_value=0, max_value=100)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0, max_value=100)
    potassium = st.number_input("Potassium (K)", min_value=0, max_value=100)

with col2:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
    ph = st.number_input("pH Level", min_value=0.0, max_value=14.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0)

# Predict Button
if st.button("Predict Crop"):
    # Prepare input data
    input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

    # Predict crop
    prediction_index = model.predict(input_data)[0]
    predicted_crop = encoder.inverse_transform([prediction_index])[0]

    st.success(f"🌱 Recommended Crop: **{predicted_crop}**")

# Footer for eco-friendly message
st.markdown("---")
st.markdown("🌍 *Supporting sustainable farming with AI*")

