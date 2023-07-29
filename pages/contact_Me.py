import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter Your Email")
    subject = st.text_input("Email subject")
    user_message = st.text_area("Write Your Message Below")
    message = f"""\
Subject: {subject}
from: {user_email}
{user_message}
"""
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(message)
        st.info("Your email wast sent successfully")

