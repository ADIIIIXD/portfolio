import streamlit as st

st.set_page_config(layout="wide")

st.title("Welcome To My Portfolio")
st.header("About Me")

cl1, cl2 = st.columns(2)

with cl1:
    st.image("images_pw/photo.png")

with cl2:
    st.title("Aditya Vikram Singh")
    content = """
    As a recent Bachelor of Commerce graduate with additional coursework in digital marketing and programming ( python ),
    I am a highly motivated and creative individual with a diverse skill set. 
    My studies in commerce have provided me with a strong foundation in business principles and practices, 
    while my coursework in digital marketing and programming have equipped me with the technical skills necessary to succeed in today's digital landscape.
    I am an ambitious and driven learner, always seeking new opportunities to challenge myself and grow. 
    In addition to my strong analytical and problem-solving skills, I am a natural motivator and leader, 
    with a talent for inspiring and guiding others towards success.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built. Feel free to contact me")
