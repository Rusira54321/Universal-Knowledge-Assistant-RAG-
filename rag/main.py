from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import os
from .chain import get_chain
from .embeddings import create_vector_store
from .embeddings import get_vector_retriever
from .loader import load_document
app = FastAPI(title="Universal RAG Assistant")

retriever = None

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_documents(files:List[UploadFile] = File(...)):
    """
    Upload multiple documents (PDF,TXT,DOCX) to build/update vector DB.
    """
    if not files:
        raise HTTPException(status_code=400,detail="No Files uploaded")
    
    all_documents = []

    for file in files:
        temp_path = os.path.join("temp_files",file.filename)
        os.makedirs("temp_files", exist_ok=True)
        with open(temp_path,"wb") as f:
            f.write(await file.read())

        try:
            docs = load_document(temp_path)
            all_documents.extend(docs)
        except ValueError as e:
            raise HTTPException(status_code=400,detail=str(e))
    global retriever    
    vector_db = create_vector_store(all_documents)
    retriever = get_vector_retriever(vector_db)
    return {"status": "success", "documents_uploaded": len(all_documents)}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Ask a question and get response using RAG chain.
    """
    if not retriever:
        raise HTTPException(status_code=400,detail="No documents uploaded yet. Please upload documents first.")
    rag_chain = get_chain(retriever)
    answer  = rag_chain.invoke(request.question)
    return JSONResponse(content={"question": request.question, "answer": answer})


# ---------------------------
# Root endpoint
# ---------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to Universal RAG Assistant! Use /upload to submit docs and /ask to query."}