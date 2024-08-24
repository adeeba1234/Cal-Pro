import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Dropdown for selecting the operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate the result based on the selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Display the result
st.write(f"Result: {result}")
