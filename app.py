import streamlit as st
import openai 
from langchain_openai import ChatOpnenAI
from langchain_core.output_parsers import StroutputParser
from langchain_core.prompts import ChatPromptTemplate


import os 
from dotenv import load_dotenv

##langsmith Traking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRAKING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot with OPENAI"

#prompt template
prompt =ChatPromptTemplate(
    [
        ("system","you are a helpful assestant .please respose to sepecic query")
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    openai.api_key=api_key
    response = openai.ChatCompletion.create(
        model=llm,
        messages=prompt.format(question=question),
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content   
