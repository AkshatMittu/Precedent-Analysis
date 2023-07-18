import streamlit as st
from utils import load_lottie
from streamlit_lottie import st_lottie

st.set_page_config(page_title='About Us', page_icon='🏛', layout='wide')

st.markdown("<h1 style='margin-top:5px;padding-top:10px;text-align: center'><u>About Us</u></h1>", unsafe_allow_html=True)
st.image("cvragain.png",width=600)
st.markdown("<h5>This application was developed as a Mini project by the students of CVR College of Engineering, Department of Emerging Technologies.</h5>", unsafe_allow_html=True)
st.write('---')


lottie = "https://assets3.lottiefiles.com/packages/lf20_ajuesHTjpJ.json"
st.header("Goal:")
animation, goal = st.columns(2)
with animation:
    lottie = load_lottie(lottie)
    st_lottie(lottie,height=350,width=350)
with goal:
    st.write("Traditionally, legal research involved manually reviewing legal documents and databases, such as court opinions, statutes, regulations, and law reviews. Lawyers and legal professionals would typically start with a broad search, using keywords and phrases related to the legal issue they are researching, and then refine their search based on the results. This process can be time-consuming and may require reviewing large volumes of legal materials to find relevant cases. Additionally, lawyers and legal professionals may consult with other lawyers or legal experts in the field to get guidance on which cases are most relevant or to identify cases that they may have missed in their initial search.")
st.write("To tackle such problems, we developed an application that has the ability to accurately and efficiently identify relevant legal cases is critical for lawyers and legal professionals. This application aims to improve the efficiency and accuracy of legal research by using text similarity algorithms to identify potentially relevant cases for a given legal opinion. It potentially reduces the time and cost needed to conduct legal research, while also increasing accessibility to legal information. It has the potential to benefit lawyers, legal professionals, and individuals who need to conduct legal research. ")

st.write('---')

st.header("Developers:")

dev1, dev2, dev3 = st.columns(3)
with dev1:
    st.markdown("<h5>Dasula Akshat Mohan</h5>", unsafe_allow_html=True)
    st.write("Roll No: 20B81A6604")
    st.write("Phone No: 955xxxxx03")
    st.write("20B81A6604@cvr.ac.in")
with dev2:
    st.markdown("<h5>Hrushitha Tigulla</h5>", unsafe_allow_html=True)
    st.write("Roll No: 20B81A6621")
    st.write("Phone No: 955xxxxx03")
    st.write("20B81A6621@cvr.ac.in")
with dev3:
    st.markdown("<h5>B. Preethika</h5>", unsafe_allow_html=True)
    st.write("Roll No: 20B81A6635")
    st.write("Phone No: 955xxxxx03")
    st.write("20B81A6635@cvr.ac.in")

st.markdown("<hr>",True)

st.markdown("<h3>Thank you for visiting our website.</h5>", unsafe_allow_html=True)
st.write("For any queries, Please email us through any of the addresses mentioned above")

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)