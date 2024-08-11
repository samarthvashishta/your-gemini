from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

## Streamlit app
st.set_page_config(page_title="GenAI APP")

st.header("Gemini LLM Application")


with st.form(key='my_form'):
    input = st.text_input("Input:", key="input")
    submit = st.form_submit_button("Ask the question")

if submit:
    response = get_gemini_response(input)
    with st.form(key='response_form'):
        st.subheader("The Response is")
        st.write(response)
        st.form_submit_button("Ask another question")