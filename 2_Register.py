import streamlit as st
import pandas as pd

df = pd.read_csv('creds.csv')
st.set_page_config(page_title='Register', page_icon='👨‍⚖️', layout='wide')

st.markdown("<h3 style='margin-top:5px;padding-top:10px;text-align: center'>Register Here:</h3>", unsafe_allow_html=True)

first,second = st.columns(2)
with first:
    username = st.text_input("Username")
    first_name = st.text_input("First Name")
    passwrd = st.text_input("Password",type="password")
    email = st.text_input("E-Mail")
with second:
    oid = st.text_input("Your Organization ID")
    last_name = st.text_input("Last Name")
    confirm_passwrd = st.text_input("Confirm Password",type="password")
    occupation = st.text_input("Occupation")
check = st.checkbox("I agree with Terms & Conditions")
if st.button('Sign Up'):
    if not all([len(i) for i in [username,oid,first_name,last_name,passwrd,confirm_passwrd,occupation,email]]):
        st.error("Please enter all credentials")
    elif passwrd != confirm_passwrd:
        st.error("Passwords don't match")
    elif '@' not in email:
        st.error('Enter valid email address')
    elif email in df['Email'].tolist():
        st.error('Email already in use')
    elif not check:
        st.error("Please agree to our Terms & Conditions")
    elif username in df['Username'].tolist():
        st.error("Username already in use")
    elif oid in df['ID'].tolist():
        st.error("ID already in use, User exists")
    elif first_name in df['First Name'].tolist() and (last_name == df['Last Name'].tolist()[df['First Name'].tolist().index(first_name)]):
        st.error('User Already exists')
    else:
        st.success("Registration Successful")
        new_data = {'First Name':first_name,'Last Name':last_name,'Password':passwrd,'ID':oid,'Occupation':occupation,'Email':email,'Username':username}
        df = df.append(new_data,ignore_index=True)
        df.to_csv('creds.csv',index=False)

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