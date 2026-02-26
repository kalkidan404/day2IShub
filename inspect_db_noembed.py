from langchain_community.vectorstores import Chroma

# use a dummy embedding to avoid downloading model
def dummy(x):
    return [0]

vs = Chroma(persist_directory="./chroma_db", embedding_function=dummy)
print("count", vs._collection.count())
print("all documents in collection:")
print(repr(vs._collection.get()))
