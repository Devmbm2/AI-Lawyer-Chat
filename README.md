# 📜 AI Lawyer Chat

An AI-powered legal document assistant that allows users to upload PDFs and ask legal questions based on the document's content.

---

## 🚀 Features
- 📄 Upload and process PDF documents
- 🔍 Retrieve relevant information using FAISS vector search
- 🤖 AI-powered responses using Groq's `deepseek-r1-distill-llama-70b` model
- 💬 Interactive chat history

---

## 📂 Project Structure
```
│── app.py                # Main Streamlit App
│── frontend.py           # Handles UI components
│── vector_store.py       # Handles vector embeddings and retrieval
│── document_processor.py # Loads & processes PDFs
│── model.py              # Handles AI model interactions
│── utils.py              # Utility functions
│── requirements.txt      # Dependencies
│── vectorstore/          # Stores FAISS index
│── pdfs/                 # Stores uploaded PDFs
│── .env                  # Environment variables
```

---

## 🛠 Installation

### ✅ Step 1: Install Dependencies
Ensure you have **Python 3.8+** installed, then install required dependencies:
```bash
pip install -r requirements.txt
```

### ✅ Step 2: Set Up API Keys
Create a `.env` file in the project root and add the following:
```
GROQ_API_KEY=your_groq_api_key
OLLAMA_MODEL=deepseek-r1:1.5b
```
Replace `your_groq_api_key` with your actual API key from [Groq](https://groq.com/).

---

## ▶️ Running the App

Run the Streamlit app using:
```bash
streamlit run app.py
```

The app will launch in your browser at **http://localhost:8501/**.

---

## 📌 Usage
1. Upload a **PDF** document.
2. Ask questions about the document.
3. View AI-generated legal responses.

---

## 🎯 Troubleshooting
- **ModuleNotFoundError?** → Run `pip install -r requirements.txt`
- **App not opening?** → Ensure Streamlit is installed:  
  ```bash
  pip install streamlit
  ```
- **Vector store not saving?** → Ensure `vectorstore/` directory exists  
  ```bash
  mkdir vectorstore
  ```

---

## 🤝 Contributing
Feel free to contribute by submitting **issues** or **pull requests**.

---

## 📜 License
MIT License

---

### 🚀 Happy Coding! 🎉
