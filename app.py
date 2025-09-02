from modules.config import OPENAI_API_KEY
from modules.data_loader import load_and_clean
from modules.eda_report import generate_profile_report
from modules.eda_summary import summarize_eda, save_summary_to_json, validate_summary_structure
from modules.vector_store import load_and_chunk_summary, build_vector_store, load_vector_store
from modules.rag_chain import get_retriever, build_rag_chain
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

df = load_and_clean("data/sales_data.csv")
generate_profile_report(df)

# Generate and save summary
summary = summarize_eda(df)
validate_summary_structure(summary)
save_summary_to_json(summary)
# print(summary)
save_summary_to_json(summary)

# Chunk and embed summary
chunks = load_and_chunk_summary()
vector_store = build_vector_store(chunks)

# load vector store
vector_store = load_vector_store()
retriever = vector_store.as_retriever()
docs = retriever.get_relevant_documents("What are the top-selling products?")
for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}:\n{doc.page_content}")

# RAG
retriever = get_retriever(vector_store)
rag_chain = build_rag_chain(retriever)

# Remove later
response = rag_chain.run("What are the top-selling products?")
print("\nRAG Response:\n", response)
