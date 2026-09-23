import chromadb
from sentence_transformers import SentenceTransformer

# Configuration

CHROMA_DB_PATH = "pdf_chroma_db"
COLLECTION_NAME = "pdf_documents"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 3
DISTANCE_THRESHOLD = 1.5

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

# Test retrieval

# query = "What is RAG?"

# results = retrieve_documents(query)

# print("\nQuery:", query)

# print("\nRetrieved Documents:")

# for document, metadata, distance in zip(
#     results["documents"][0],
#     results["metadatas"][0],
#     results["distances"][0]
# ):
#     print("\nDocument:")
#     print(document)

#     print("\nMetadata:")
#     print(metadata)

#     print("Distance:", distance)


if __name__ == "__main__":

    queries = [
        "What is RAG?",
        "What is the capital of Japan?"
    ]

    for query in queries:

        print("\n" + "=" * 50)
        print("Query:", query)

        results = retrieve_documents(query)

        for document, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            print("\nPage:", metadata["page"])
            print("Distance:", distance)
            print("Document:", document[:100])