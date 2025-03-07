import streamlit as st
from document_processor import upload_pdf, load_and_process_pdf
from vector_store import create_vector_store, retrieve_docs
from model import answer_query
import os

st.set_page_config(page_title="AI Lawyer Chat", layout="wide")

# Session State Initialization
if "faiss_db" not in st.session_state:
    st.session_state["faiss_db"] = None
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.title("📜 AI Lawyer Chat")
col1, col2 = st.columns([0.3, 0.7])

with col1:
    st.subheader("📄 Document Processing")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=False)
    reset_chat = st.button("🔄 Reset & Upload New Document")

    if reset_chat:
        st.session_state["faiss_db"] = None
        st.session_state["chat_history"] = []
        st.rerun()

    if uploaded_file and st.session_state["faiss_db"] is None:
        with st.spinner("Processing document..."):
            file_path = upload_pdf(uploaded_file)
            text_chunks = load_and_process_pdf(file_path)
            st.session_state["faiss_db"] = create_vector_store("vectorstore/db_faiss", text_chunks)
        st.success("PDF Processed Successfully! You can now ask questions.")

st.divider()

with col2:
    st.subheader("💬 Chat History")
    for role, message in st.session_state["chat_history"]:
        with st.chat_message(role):
            st.write(message)
    
    user_query = st.chat_input("Ask your legal question...")
    
    if user_query and st.session_state["faiss_db"]:
        retrieved_docs = retrieve_docs(st.session_state["faiss_db"], user_query)
        response = answer_query(retrieved_docs, user_query)
        
        st.session_state["chat_history"].append(("You", user_query))
        st.session_state["chat_history"].append(("AI Lawyer", response))
        
        st.rerun()
