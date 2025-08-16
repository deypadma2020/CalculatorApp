import streamlit as st
import requests

st.set_page_config(page_title="Calculator API UI", layout="centered")
st.title("🧮 FastAPI-Powered Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for operation
operation = st.selectbox("Choose Operation", ["add", "sub", "mul", "div"])

# Backend API base URL
API_URL = "http://localhost:8000/api/v1"

# Submit button
if st.button("Calculate"):
    payload = {"a": num1, "b": num2}

    try:
        # Send request to FastAPI backend based on selected operation
        response = requests.post(f"{API_URL}/{operation}", json=payload)
        response.raise_for_status()
        result = response.json().get("result")

        st.success(f"✅ Result: {result}")

    except requests.exceptions.HTTPError as http_err:
        st.error(f"❌ HTTP error: {http_err}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
