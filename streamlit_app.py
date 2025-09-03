import os
import json
import streamlit as st
from modules.query_logger import log_query


from modules.config import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from modules.vector_store import load_vector_store
from modules.rag_chain import get_retriever, build_rag_chain

st.set_page_config(page_title="BizWitz AI", layout="centered")
st.title("BizWitz AI Assistant")

# Input field for user query
query = st.text_input("Ask a question about your sales data:")

# Load vector store and build RAG chain
vector_store = load_vector_store()
retriever = get_retriever(vector_store)
rag_chain = build_rag_chain(retriever)


if st.button("Run Query") and query:
    response = rag_chain.run(query)
    log_query(query, response)
    st.subheader("Response")
    st.write(response)


# EDA summary
try:
    with open("reports/eda_summary.json") as f:
        eda_summary = json.load(f)

    with st.expander("View EDA Summary"):
        st.json(eda_summary)
except FileNotFoundError:
    st.warning("EDA summary file not found. Please run the backend pipeline first.")