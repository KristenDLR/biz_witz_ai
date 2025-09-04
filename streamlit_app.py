import os
import json
import streamlit as st
import streamlit.components.v1 as components

from modules.query_logger import log_query
from modules.config import OPENAI_API_KEY
from modules.vector_store import load_vector_store
from modules.rag_chain import get_retriever, build_rag_chain

# Set OpenAI key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Streamlit UI config
st.set_page_config(page_title="BizWitz AI", layout="centered")
st.title("BizWitz AI Assistant")

# Query input
query = st.text_input("Ask a question about your sales data:")

# Load vector store and build RAG chain
vector_store = load_vector_store()
retriever = get_retriever(vector_store)
rag_chain = build_rag_chain(retriever)

# Run query
if st.button("Run Query") and query:
    response = rag_chain.run(query)
    log_query(query, response)
    st.subheader("Response")
    st.write(response)

# Display EDA summary (JSON)
try:
    with open("reports/eda_summary.json") as f:
        eda_summary = json.load(f)
    with st.expander("View EDA Summary (JSON)"):
        st.json(eda_summary)
except FileNotFoundError:
    st.warning("EDA summary file not found. Please run the backend pipeline first.")

# Display full EDA report (HTML)
try:
    with open("reports/eda_report.html", "r") as f:
        report_html = f.read()
    with st.expander("View Full EDA Report (Graphs & Visuals)"):
        components.html(report_html, height=1000, scrolling=True)
except FileNotFoundError:
    st.warning("EDA HTML report not found. Please run the backend pipeline first.")
