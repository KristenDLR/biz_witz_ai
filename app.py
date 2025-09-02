from modules.config import OPENAI_API_KEY
from modules.data_loader import load_and_clean
from modules.eda_report import generate_profile_report, summarize_eda
from modules.eda_summary import save_summary_to_json
from modules.vector_store import load_and_chunk_summary, build_vector_store, load_vector_store
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

df = load_and_clean("data/sales_data.csv")
generate_profile_report(df)

# Generate and save summary
summary = summarize_eda(df)
# print(summary)
save_summary_to_json(summary)

# Chunk and embed summary
chunks = load_and_chunk_summary()
vector_store = build_vector_store(chunks)


vector_store = load_vector_store()
retriever = vector_store.as_retriever()
docs = retriever.get_relevant_documents("What are the top-selling products?")
for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}:\n{doc.page_content}")
