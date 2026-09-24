import chromadb
from sentence_transformers import SentenceTransformer
from app.config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K,
    DISTANCE_THRESHOLD
)

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

    # Filter results using distance threshold

    filtered_documents = []
    filtered_metadatas = []
    filtered_distances = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):

        if distance < DISTANCE_THRESHOLD:
            filtered_documents.append(document)
            filtered_metadatas.append(metadata)
            filtered_distances.append(distance)

    return {
        "documents": [filtered_documents],
        "metadatas": [filtered_metadatas],
        "distances": [filtered_distances]
    }
