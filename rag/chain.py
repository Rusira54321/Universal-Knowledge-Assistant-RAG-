from langchain_core.runnables import RunnablePassthrough
from .prompts import get_qa_prompt
from .llm import get_llm
from .embeddings import get_vector_retriever
from .embeddings import create_vector_store
from langchain_chroma import Chroma


def get_chain(Documents,vectorDb:Chroma,llm,retriever):
    llm
    prompt = get_qa_prompt()
    retriever
    rag_Chain  = (
            {
                "context":retriever,
                "question":RunnablePassthrough(),
            }
            |
            prompt
            |
            llm
        )
    return rag_Chain

