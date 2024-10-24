import streamlit as st

# Title for the calculator
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", step=0.01)
num2 = st.number_input("Enter the second number:", step=0.01)

# Dropdown menu to select an operation
operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on the selected operation
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

# Display result
st.write(f"The result is: {result}")
