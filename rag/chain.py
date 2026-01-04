from langchain_core.runnables import RunnablePassthrough,RunnableLambda
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
                 # 👇 extract only question for retriever
                "context": RunnableLambda(lambda x: x["question"]) | retriever,
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

