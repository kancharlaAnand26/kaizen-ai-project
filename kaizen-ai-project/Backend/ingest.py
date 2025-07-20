import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

PERSIST_DIRECTORY = 'chroma_db'
SOURCE_DIRECTORY = 'documents'

def main():
    print("🚀 Starting data ingestion...")

    # Load documents from the source directory
    loader = DirectoryLoader(
        SOURCE_DIRECTORY,
        glob="**/*",
        loader_map={".pdf": PyPDFLoader, ".txt": TextLoader},
        show_progress=True
    )
    documents = loader.load()

    if not documents:
        print("No documents found. Please add manuals to the 'documents' folder.")
        return

    print(f"✅ Loaded {len(documents)} document(s).")

    # Split documents into smaller, manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    print(f"✅ Split documents into {len(texts)} chunks.")

    # Generate embeddings for each chunk
    print("🧠 Generating embeddings... (this may take a moment)")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Create and persist the Chroma vector store
    print(f"💾 Creating and saving vector store in '{PERSIST_DIRECTORY}'...")
    db = Chroma.from_documents(texts, embeddings, persist_directory=PERSIST_DIRECTORY)
    
    print("🎉 Ingestion complete! The knowledge base is ready.")

if __name__ == "__main__":
    main()