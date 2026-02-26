from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import os
# -----------------------------------------
# 1️⃣ Sample Documents
# -----------------------------------------

documents = [
    "i am kalkidan shewit learning IS at AAU.",
    "the project about RAG and vector database by IS hub",
    "the exprience i had with IS and RAG is very good and i am learning a lot.",
    "the acheivements i had over this short time with RAG workshop is out standing i learned the fundamental knowledges to persuie it.",
    "my long term GOAL is deciding my framework and learning it and make a project with it.",
]

docs = [Document(page_content=text) for text in documents]

# -----------------------------------------
# 2️⃣ Load Embedding Model
# -----------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------------------
# 3️⃣ Create Vector Store
# -----------------------------------------

persist_dir = "./chroma_db"

# ------------------------------------------------------------------
# for this simple demo we don't want stale/duplicate entries
# every time the script runs, so delete the folder if it exists
# (in a production app you might keep the store and instead check
# for duplicates before inserting new documents).
# ------------------------------------------------------------------
import shutil
if os.path.exists(persist_dir):
    print(f"removing existing store at {persist_dir} to avoid duplicates")
    shutil.rmtree(persist_dir)

# always build from scratch for the sample documents
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory=persist_dir
)
vector_store.persist()

# -----------------------------------------
# 4️⃣ Similarity Search Function
# -----------------------------------------

def search_query(query, top_k=1):
    print(f"\n🔎 Query: {query}")
    print(f"Top-K: {top_k}")

    results = vector_store.similarity_search(query, k=top_k)

    for i, result in enumerate(results):
        print(f"\nResult {i+1}:")
        print(result.page_content)

# -----------------------------------------
# 5️⃣ Run Example Searches
# -----------------------------------------

search_query("Who am i", top_k=2)
search_query("what is my long term goal?", top_k=3)