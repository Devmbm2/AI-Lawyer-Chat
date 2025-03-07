import streamlit as st

def reset_chat():
    """Reset chat history and FAISS database."""
    st.session_state["faiss_db"] = None
    st.session_state["chat_history"] = []
    st.rerun()
