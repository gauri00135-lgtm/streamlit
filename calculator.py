
import streamlit as st
st.title("Simple Calculator")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

op = st.selectbox("Choose operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if op == "+":
        st.success(a + b)
    elif op == "-":
        st.success(a - b)
    elif op == "*":
        st.success(a * b)
    elif op == "/":
        if b != 0:
            st.success(a / b)
        else:
            st.error("Division by zero not allowed")