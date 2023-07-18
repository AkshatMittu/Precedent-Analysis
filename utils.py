import numpy as np
import pandas as pd
import string
import re
import tensorflow_hub as hub
from num2words import num2words
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from fpdf import FPDF
import requests
import streamlit as st

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        st.write("Didnt get")
        return None
    return r.json()

df = pd.read_csv('embeddings.csv')
text_df = pd.read_csv('scotus_cleaned_again.csv')

df = df.drop('Unnamed: 0',axis=1)

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
use = hub.load(module_url)

svm = joblib.load('Embedding_Model.joblib')

def preprocess_for_embedding(text):
    
    text = text.lower()
    contractions = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is", "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are", "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have", "you'd": "you would",
                "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}
    text = ' '.join([contractions[word] if word in contractions else word for word in text.split()])
    text = re.sub(r'[^0-9a-zA-Z\s]+','',text)
    text = text.translate(str.maketrans('','',string.punctuation))
    text = ' '.join([num2words(word) if word.isdigit() else word for word in text.split()])
    while re.search('-',text):
        text = re.sub('-',' ',text)
    while re.search(',',text):
        text = re.sub(',',' ',text)
    return text

def citations_using_embeddings(text,use,df,text_df,svm):
    predicted_df = pd.DataFrame(columns = text_df.columns)
    text = preprocess_for_embedding(text)
    ls = use([text])
    prediction = svm.predict(ls)[0]
    new_df = df[df['label']==prediction].drop('label',axis=1)
    distances = []
    for i,row in new_df.iterrows():
        array = np.array(row)
        distances.append((np.linalg.norm(ls-array),i))
    print("\nCosine Similarity\n")  
    sim = cosine_similarity(X = df.drop('label',axis=1),Y = ls)
    predicted_df = predicted_df.append(text_df.iloc[np.argmax(sim)])
    print("Using SVM\n")
    for _,i in sorted(distances)[:6]:
        predicted_df = predicted_df.append(text_df.iloc[i])
    predicted_df = predicted_df.drop_duplicates()
    return sorted(distances)[:10],np.argmax(sim),predicted_df

def generate_pdf(file_name,df,i):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial","BU",16)
    pdf.cell(0,9,f"Case Name: {df.iloc[i]['case_name'].title()}",ln=1,align="C")
    pdf.cell(84,10,"",ln=1)
    pdf.set_font("Arial","B",13)
    pdf.cell(60,6,"Author Name:")
    pdf.set_font("Arial","",13)
    pdf.cell(45,6,f"{df.iloc[i]['author_name'].title()}",ln=1)
    pdf.set_font("Arial","B",13)
    pdf.cell(60,7,"Category:")
    pdf.set_font("Arial","",13)
    pdf.cell(45,7,f"{df.iloc[i]['category'].title()}",ln=1)
    pdf.set_font("Arial","B",13)
    pdf.cell(60,7,"Date Filed:")
    pdf.set_font("Arial","",13)
    pdf.cell(45,7,f"{df.iloc[i]['date_filed'].title()}",ln=1)
    pdf.set_font("Arial","B",13)
    pdf.cell(60,7,"Case Descrption:")
    pdf.set_font("Arial","",13)
    text=df.iloc[i]['text'].encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0,5,f"{text}")
    pdf.output(f'{file_name}.pdf')
    
    
def scaling(given):
    distances = np.array(given)
    max_dist = np.max(distances)
    scaled_distances = (max_dist - distances)
    return scaled_distances