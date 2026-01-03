from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .llm import get_embedding_model

def create_vector_store(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400,chunk_overlap=50)
    splites = text_splitter.split_documents(documents)
    vectordb = Chroma.from_documents(
        documents=splites,
        embedding=get_embedding_model()
    )
    return vectordb

def get_vector_retriever(vectordb:Chroma):
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    return retriever

