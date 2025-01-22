import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Fetch the GROQ API key
groq_api_key = os.getenv("GROQ_API")

# Initialize the model and parser
model = ChatGroq(model="Gemma2-9b-it", groq_api_key=groq_api_key)
parser = StrOutputParser()

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following into language:{language}"),
        ("user", "text:{text}"),
    ]
)

# Define the LangChain pipeline
chain = prompt | model | parser

# Streamlit app UI
st.title("LangChain Translation App")
st.title("English to other Language")
st.write("Translate text into your desired language using LangChain and Groq AI.")

# User input for the text to be translated
text = st.text_area(
    "Enter the text to be translated:", placeholder="Type your text here..."
)

# User input for the target language
language = st.text_input(
    "Enter the target language:", placeholder="e.g., French, Spanish, etc."
)

# Button to run the translation
if st.button("Translate"):
    if text and language:
        # Run the LangChain pipeline
        input_data = {"text": text, "language": language}
        try:
            result = chain.invoke(input_data)
            st.success(f"Translated Text: {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both text and target language.")

# Footer
st.write("Powered by LangChain, Groq AI, and Streamlit. Created by Prashant More")
