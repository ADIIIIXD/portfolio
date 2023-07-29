import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter Your Email")
    user_message = st.text_area("Write Your Message Below")
    submit = st.form_submit_button("Submit")
