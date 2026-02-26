from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vs = Chroma(persist_directory="./chroma_db", embedding_function=emb)
print("count", vs._collection.count())
print("entries:")
for doc in vs._collection.get():
    print(doc)
