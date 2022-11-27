import streamlit as st
import pickle
import string
import nltk

model=pickle.load(open('model.pkl','rb'))
st.title("SMS Classifier")
input_sms= st.text_area("Enter the message")
#print(input_sms)
text=[]
v={2:'Fund Transfer',0: 'Login OTP',1: 'Password reset OTP',4: 'SPAM',3: 'HAM'}
text.append(input_sms)
if st.button("Predict"):
    result=model.predict(text)
    
    st.header(v[result[0]])


