import streamlit as st
from utils import load_lottie
from streamlit_lottie import st_lottie
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

lottie = "https://assets8.lottiefiles.com/packages/lf20_rdkrsaca.json"

st.set_page_config(page_title='Login', page_icon='⚖', layout='wide')
df = pd.read_csv('creds.csv')
st.markdown("<h1 style='margin-top:5px;padding-top:10px;text-align: center'>Precendent Analysis</h1>", unsafe_allow_html=True)
lottie = load_lottie(lottie)
first,second = st.columns(2)
with first:
    st_lottie(lottie,height=350,width=350)
with second:
    user = st.text_input("Username")
    passwrd = st.text_input("Password",type="password")
    st.write('##')
    if st.button('Login'):
        if len(user) == 0 or len(passwrd) == 0:
            st.error('Please enter credentials') 
        elif user in df['Username'].tolist() and (passwrd == str(df['Password'].tolist()[df['Username'].tolist().index(user)])):
            st.success("Login Successful")
            details = df[df['Username'] == user]    
            st.session_state['username'] = user
            st.session_state['occupation'] = details['Occupation'][0]
            st.session_state['id'] = details['ID'][0]
            st.session_state['email'] = details['Email'][0]
            switch_page('Case')
        else:
            st.error("Login Failed")
    text,register = st.columns([1,1])
    with text:
        st.markdown("<p style='padding-top:5px;text-align: center'>Don't have an account?</p>", unsafe_allow_html=True)
    with register:
        if st.button('Register'):
            switch_page('Register')

logout = st.sidebar.button('Logout')
if logout and len(st.session_state) != 0:
    st.session_state.clear()
    st.sidebar.success("Sign out successful")
elif logout and len(st.session_state) == 0:
    st.sidebar.error("Please login first")

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)