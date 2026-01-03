import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load .env ONCE when module is imported
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY not found. Please set it in your .env file."
    )

def get_llm(model_name: str = "gpt-4o-mini", temperature: float = 0.0):
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
    )
    return llm

def get_embedding_model(model_name: str = "text-embedding-3-small"):
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    embedding_model = OpenAIEmbeddings(model=model_name)
    return embedding_model



