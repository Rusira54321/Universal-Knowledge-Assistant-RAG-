# Universal RAG Assistant

A **Retrieval-Augmented Generation (RAG) assistant** built with **FastAPI**, **LangChain**, and **OpenAI**.  
This application allows you to upload documents (PDF, TXT, DOCX) to create a vector database, and then query the knowledge base with natural language questions.

---

## Features

- Upload multiple documents to build/update a vector store
- Ask questions using an intelligent assistant powered by RAG
- Maintains chat history for context-aware responses
- Built-in support for multiple file types: PDF, TXT, DOCX
- CORS enabled to work with frontend apps (e.g., Vercel)
- Modular design with LangChain chains and embeddings

---

## Tech Stack

- **Backend**: FastAPI  
- **Vector Store**: Chroma  
- **Embeddings**: OpenAI Embeddings (`text-embedding-3-small`)  
- **LLM**: OpenAI Chat LLM (`gpt-4o-mini`)  
- **Document Loaders**: PyPDFLoader, TextLoader, Docx2txtLoader  
- **Frontend Compatibility**: Any JS/React frontend (CORS enabled)  

---

## Installation

1. Clone the repository
```
git clone https://github.com/<your-username>/<repo-name>
.git
cd <repo-name>
```
2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Create .env file
```
  Add your OpenAI API key:OPENAI_API_KEY=your_openai_api_key_here
```
---
## Usage
1. Run locally

```
uvicorn rag.main:app --reload --host 0.0.0.0 --port 8000
FastAPI docs: http://127.0.0.1:8000/docs
```

2. Upload documents

```
Endpoint: POST /upload
Form-data: files (multiple PDF, TXT, or DOCX)
Example using curl:
    curl -X POST "http://127.0.0.1:8000/upload" \
    -F "files=@example.pdf" \
    -F "files=@example.txt"
```

3. Ask a question
```
Endpoint: POST /ask

JSON body:

{
  "question": "Who is Albert Einstein?"
}
Response:

{
  "question": "Who is Albert Einstein?",
  "answer": "Albert Einstein was a theoretical physicist who developed the theory of relativity..."
}

```
---
## Project Structure

```
RAGProject/
├─ rag/
│  ├─ __init__.py
│  ├─ main.py          # FastAPI app
│  ├─ chain.py         # RAG chains
│  ├─ embeddings.py    # Vector store & retriever
│  ├─ loader.py        # Document loaders
│  ├─ llm.py           # OpenAI LLM and embeddings
│  └─ prompts.py       # QA and rewrite prompts
├─ requirements.txt
├─ .env
└─ README.md
```
---
## Deployment

```
You can deploy this project on Render or any cloud provider:
Make sure the FastAPI server runs with:
uvicorn rag.main:app --host 0.0.0.0 --port $PORT
Add CORS origins for your frontend domains.
Set OPENAI_API_KEY in environment variables.
```
---
## Notes

```
   1.) chunk_size and chunk_overlap in vector store creation are set to 700 and 90 respectively for optimal context retrieval.

   2.)Chat history is maintained globally for session-based context.

   3.)Only PDF, TXT, and DOCX are supported.
```
---
## License

```
This project is licensed under the MIT License.
```
---
## Acknowledgements

```
   LangChain – for building RAG pipelines
   OpenAI– for embeddings and LLM
   FastAPI– backend framework
   Chroma– vector database
```


   
