from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def get_retriever(vector_store):
    return vector_store.as_retriever(search_kwargs={"k": 3})

def build_rag_chain(retriever):
    llm = ChatOpenAI()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)