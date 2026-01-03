import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
OPENAI_API_KEY = os.getenv("OPENAI_KEY")


def get_llm(model_name: str = "gpt-4o-mini", temperature: float = 0.0):
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
    )
    return llm

def get_embedding_model(model_name: str = "text-embedding-3-small"):
    embedding_model = OpenAIEmbeddings(model=model_name)
    return embedding_model



