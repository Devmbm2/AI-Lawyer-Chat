from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# Model for embeddings
ollama_model_name = "deepseek-r1:1.5b"
embeddings_model = OllamaEmbeddings(model=ollama_model_name)

def create_vector_store(db_path, text_chunks):
    """Create and save FAISS vector store."""
    faiss_db = FAISS.from_documents(text_chunks, embeddings_model)
    faiss_db.save_local(db_path)
    return faiss_db

def retrieve_docs(faiss_db, query):
    """Retrieve similar documents from FAISS DB."""
    return faiss_db.similarity_search(query)
