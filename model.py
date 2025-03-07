from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

custom_prompt_template = """
Use the pieces of information provided in the context to answer the user's question.
If you don't know the answer, just say that you don't know. Don't provide anything out of the given context.

Question: {question} 
Context: {context} 
Just return the final answer:
"""

llm_model = ChatGroq(model="deepseek-r1-distill-llama-70b")

def get_context(documents):
    """Extract context text from retrieved documents."""
    return "\n\n".join([doc.page_content for doc in documents])

def answer_query(documents, query):
    """Generate an answer based on retrieved documents."""
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | llm_model
    response = chain.invoke({"question": query, "context": context})
    return response.content.strip().split("\n")[-1]  # Extract only the final answer
