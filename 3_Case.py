import streamlit as st
from utils import load_lottie
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page



lottie = "https://assets2.lottiefiles.com/packages/lf20_6ljswtij.json"
st.set_page_config(page_title='Case Description', page_icon='📄', layout='wide')

st.markdown("<h1 style='margin-top:5px;padding-top:10px;text-align: center'>Enter Case Description</h1>", unsafe_allow_html=True)
lottie = load_lottie(lottie)
animation, descrip = st.columns(2)
with animation:
    st_lottie(lottie,height=200,width=200)
with descrip:
    description = st.text_area(label='Case Description')
    clicked = st.button("Submit")


if len(description) != 0:
    from utils import citations_using_embeddings, df, text_df, use, svm, generate_pdf, scaling
    distances,similarity,precedents = citations_using_embeddings(description,use,df,text_df,svm)
    
    scaled = scaling([i for i,_ in distances])
    
    st.write('---')
    st.write("## Most Relevant Case:")
    st.markdown(f"<h4><u>{precedents.iloc[0]['case_name']}</u></h4>", unsafe_allow_html=True)
    st.write(f"{precedents.iloc[0]['author_name'].title()}")
    st.write(f"{precedents.iloc[0]['date_filed']}")
    st.write(f"Link: {precedents.iloc[0]['absolute_url']}")
    # case1 = st.progress(0,text="Relevance")
    # case1.progress(float(similarity),text='Relevance')
    if st.button("Download PDF",key=0):
        generate_pdf(f"{precedents.iloc[0]['case_name']}_{st.session_state['username']}",precedents,0)
            
    st.write('---')  
    st.write("## Other relevant cases:")
    one,two= st.columns(2)
    with one:
        st.markdown(f"<h4><u>{precedents.iloc[1]['case_name']}</u></h4>", unsafe_allow_html=True)
        st.write(f"{precedents.iloc[1]['author_name'].title()}")
        st.write(f"{precedents.iloc[1]['date_filed']}")
        st.write(f"Link: {precedents.iloc[1]['absolute_url']}")
        case2 = st.progress(0,text="Relevance")
        case2.progress(int(scaled[0]*100),text='Relevance')
        if st.button("Download PDF",key=1):
            generate_pdf(f"{precedents.iloc[1]['case_name']}_{st.session_state['username']}",precedents,1)
    with two:
        st.markdown(f"<h4><u>{precedents.iloc[2]['case_name']}</u></h4>", unsafe_allow_html=True)
        st.write(f"{precedents.iloc[2]['author_name'].title()}")
        st.write(f"{precedents.iloc[2]['date_filed']}")
        st.write(f"Link: {precedents.iloc[2]['absolute_url']}")
        case3 = st.progress(0,text="Relevance")
        case3.progress(int(scaled[1]*100),text='Relevance')
        if st.button("Download PDF",key=2):
            generate_pdf(f"{precedents.iloc[2]['case_name']}_{st.session_state['username']}",precedents,2)
    three,four= st.columns(2)
    with three:
        st.markdown(f"<h4><u>{precedents.iloc[3]['case_name']}</u></h4>", unsafe_allow_html=True)
        st.write(f"{precedents.iloc[3]['author_name'].title()}")
        st.write(f"{precedents.iloc[3]['date_filed']}")
        st.write(f"Link: {precedents.iloc[3]['absolute_url']}")
        case4 = st.progress(0,text="Relevance")
        case4.progress(int(scaled[2]*100),text='Relevance')
        if st.button("Download PDF",key=3):
            generate_pdf(f"{precedents.iloc[3]['case_name']}_{st.session_state['username']}",precedents,3)
    with four:
        st.markdown(f"<h4><u>{precedents.iloc[4]['case_name']}</u></h4>", unsafe_allow_html=True)
        st.write(f"{precedents.iloc[4]['author_name'].title()}")
        st.write(f"{precedents.iloc[4]['date_filed']}")
        st.write(f"Link: {precedents.iloc[4]['absolute_url']}")
        case5 = st.progress(0,text="Relevance")
        case5.progress(int(scaled[3]*100),text='Relevance')
        if st.button("Download PDF",key=4):
            generate_pdf(f"{precedents.iloc[4]['case_name']}_{st.session_state['username']}",precedents,4)
    
try:
    
    st.sidebar.markdown(f"<h2>Welcome, {st.session_state['username']}</h2>",unsafe_allow_html=True)
    st.sidebar.write(f"ID: {st.session_state['id']+1}")
    st.sidebar.write(f"Occupation: {st.session_state['occupation']}")
    st.sidebar.write(f"Email: {st.session_state['email']}")
    logout = st.sidebar.button('Logout')
    if logout and len(st.session_state) != 0:
        st.session_state.clear()
        switch_page("Login")
    elif logout and len(st.session_state) == 0:
        st.sidebar.error("Please login first")

except:
    switch_page("Login")


hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)