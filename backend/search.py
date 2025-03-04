from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

# Initialize Vector Database
vector_db = Chroma(persist_directory="./db", embedding_function=OpenAIEmbeddings())
retriever = vector_db.as_retriever()

# OpenAI LLM
llm = OpenAI(model_name="gpt-4", temperature=0.7)

def search_query(query: str):
    response = retriever.get_relevant_documents(query)
    return {"results": [doc.page_content for doc in response]}