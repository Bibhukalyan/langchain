from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import create_retrieval_chain

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
#Langsmith Tracing
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

##Streamlit Framework
st.title("Langchain demo with FAISS, Huggingface embadding and LLAMA3")
doc_text=st.text_input("Enter the url to be analyzed:")
input_text=st.text_input("What question you have in mind?")
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
##LLAMA3 model
llm=Ollama(model="LLAMA3.2")
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    """
)
## Document chain
document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

##Data Ingestion -- From the website we need to scrap the data
if doc_text:
    loader = WebBaseLoader(doc_text)
    data = loader.load()
    ## Convert the data to chunks
    all_splits = text_splitter.split_documents(data)
    db = FAISS.from_documents(all_splits, embeddings)
    retriver=db.as_retriever()
    retrival_chain=create_retrieval_chain(retriver, document_chain)

if st.button("Analyze"):
    if input_text:
         st.write(retrival_chain.invoke({"input":input_text})["answer"])


