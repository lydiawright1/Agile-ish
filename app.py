import streamlit as st

st.title("Hello Databricks!")

st.write("This is a basic Streamlit app running on Databricks.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

if st.button("Click me"):
    st.balloons()
    st.success("Button clicked!")
