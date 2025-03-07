import streamlit as st

def display_chat_history(chat_history):
    """Display chat messages in Streamlit."""
    st.subheader("💬 Chat History")
    for role, message in chat_history:
        with st.chat_message(role):
            st.write(message)
