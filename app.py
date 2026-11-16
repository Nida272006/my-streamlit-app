import streamlit as st

st.title("Welcome to My First Streamlit App")

st.write("This is my first Python Streamlit application.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success("Hello, " + name + "!")
    else:
        st.warning("Please enter your name.")