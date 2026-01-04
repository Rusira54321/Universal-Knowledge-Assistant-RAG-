from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from .prompts import get_qa_prompt
from .llm import get_llm
from .embeddings import get_vector_retriever
from .embeddings import create_vector_store
from langchain_core.output_parsers import StrOutputParser
from .prompts import re_write_question_prompt
rewrite_prompt = re_write_question_prompt()
llm = get_llm()
parser = StrOutputParser()
def get_chain(retriever):
    llm
    prompt = get_qa_prompt()
    retriever
    rag_Chain  = (
            {
                 # 👇 extract only question for retriever
                "context": retriever,
                "question": RunnableLambda(lambda x: x["question"]),
                "chat_history": RunnableLambda(lambda x: x["chat_history"]),
            }
            |
            prompt
            |
            llm
            |
            parser
        )
    return rag_Chain

def get_retriever_chain(retriever):
    history_aware_retriever = (
        rewrite_prompt
        |
        llm
        |
        (lambda x:x.content)
        |
        retriever
    )
    return history_aware_retriever

