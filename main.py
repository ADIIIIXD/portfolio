import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Welcome To My Portfolio")
st.header("About Me")

st.markdown("""<hr style="height:3px;border:none;color:#FFFF00;background-color:#FFFF00;" /> """,
            unsafe_allow_html=True)

cl1, cl2 = st.columns(2)

with cl1:
    st.image("images/adi.png", width=400)

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

st.markdown("""<hr style="height:3px;border:none;color:#FFFF00;background-color:#FFFF00;" /> """,
            unsafe_allow_html=True)

st.write("<h3><p style='font-family: Abril Fatface; color:Purple; font-size: 42px'>"
         "Below you can find some of the apps I have built.</p></h3>",
         unsafe_allow_html=True)

st.markdown("""<hr style="height:3px;border:none;color:#FFFF00;background-color:#FFFF00;" />""",
            unsafe_allow_html=True)

df = pandas.read_csv("data.csv", sep=";")

cl3, emp_col,  cl4 = st.columns([1.5, 0.5, 1.5])

with cl3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"],)
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[SOURCE CODE]({row['url']})")

with cl4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[SOURCE CODE]({row['url']})")
