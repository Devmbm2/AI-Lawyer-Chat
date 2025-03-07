import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdfs_directory = "pdfs/"

def upload_pdf(file):
    """Save uploaded PDF to the `pdfs/` directory."""
    os.makedirs(pdfs_directory, exist_ok=True)
    file_path = os.path.join(pdfs_directory, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

def load_and_process_pdf(file_path):
    """Load and split PDF text into chunks."""
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    return text_splitter.split_documents(documents)
