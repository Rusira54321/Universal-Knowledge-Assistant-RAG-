from langchain_core.runnables import RunnablePassthrough
from .prompts import get_qa_prompt
from .llm import get_llm
from .embeddings import get_vector_retriever
from .embeddings import create_vector_store
from langchain_core.output_parsers import StrOutputParser
llm = get_llm()
parser = StrOutputParser()
def get_chain(retriever):
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
            |
            parser
        )
    return rag_Chain

