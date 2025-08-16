import streamlit as st

st.set_page_config(page_title="Calculator UI", layout="centered")
st.title("🧮 Standalone Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown for operation
operation = st.selectbox("Choose Operation", ["add", "sub", "mul", "div"])

# Submit button
if st.button("Calculate"):
    try:
        result = None
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                st.error("❌ Division by zero is not allowed")
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"✅ Result: {result}")

    except Exception as e:
        st.error(f"❌ Error: {e}")
