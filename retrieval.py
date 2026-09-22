import chromadb
from sentence_transformers import SentenceTransformer

# Configuration

CHROMA_DB_PATH = "pdf_chroma_db"
COLLECTION_NAME = "pdf_documents"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 3

# Load embedding model

model = SentenceTransformer(EMBEDDING_MODEL)

# Connect to ChromaDB

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH
)

collection = client.get_collection(
    name=COLLECTION_NAME
)

# Retrieval function

def retrieve_documents(query):

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=TOP_K
    )

    return results

# Test retrieval

query = "What is RAG?"

results = retrieve_documents(query)

print("\nQuery:", query)

print("\nRetrieved Documents:")

for document, metadata, distance in zip(
    results["documents"][0],
    results["metadatas"][0],
    results["distances"][0]
):
    print("\nDocument:")
    print(document)

    print("\nMetadata:")
    print(metadata)

    print("Distance:", distance)