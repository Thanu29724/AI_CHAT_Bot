import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

st.title("AI Assistant 🤖")

user_input = st.text_input("Ask a question:")

if user_input:
    response = llm.invoke(user_input)
    st.write(response.content)