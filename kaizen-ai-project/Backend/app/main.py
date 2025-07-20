import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Load environment variables from .env file
load_dotenv()

# Check for OpenAI API Key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Initialize FastAPI app
app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic model for the request body
class ChatRequest(BaseModel):
    query: str

# Setup for the RAG chain
PERSIST_DIRECTORY = 'chroma_db'
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3}) # Retrieve top 3 relevant chunks
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Custom prompt template
prompt_template = """
Use the following pieces of context from the technical manual to answer the user's question.
Your role is a helpful expert assistant for Meidensha Corporation.
If you don't find the answer in the provided context, just say that the information is not available in the manual. Do not try to make up an answer.
Provide a clear, concise, and step-by-step answer if possible.

Context: {context}

Question: {question}

Helpful Answer:
"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt_template)

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    Handles chat requests by querying the RAG chain.
    """
    query = request.query
    if not query:
        return {"error": "Query cannot be empty"}
    
    print(f"Received query: {query}")
    result = qa_chain.invoke({"query": query})
    
    return {"answer": result['result']}

@app.get("/")
def read_root():
    return {"message": "KAIZEN-AI Backend is running"}