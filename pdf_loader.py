from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

# Configuration
PDF_PATH ="rag_guide.pdf"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# PDF Text Extraction

reader = PdfReader(PDF_PATH)

print("Number of pages:", len(reader.pages))

# full_text = ""

# for page_number, page in enumerate(reader.pages, start=1):
#     text = page.extract_text()

#     if text:
#         full_text += text + "\n"

# print(f"\n--- Full PDF Text ---")
# print(full_text)

# Text Chunking

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

# Generate page-level chunks

all_chunks = []
all_metadatas = []

for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text()

    if not text:
        continue

    page_chunks = text_splitter.split_text(text)

    for chunk in page_chunks:

        all_chunks.append(chunk)

        all_metadatas.append({
            "source": PDF_PATH,
            "page" : page_number
        })

print("\nNumber of chunks:", len(all_chunks))


# Generate Embeddings

model = SentenceTransformer(EMBEDDING_MODEL)

embeddings = model.encode(all_chunks)

print("\nEmbedding shape:", embeddings.shape)


# ChromaDB

client = chromadb.PersistentClient(
    path="pdf_chroma_db"
    )

collection = client.get_or_create_collection(
    name="pdf_documents"
)

# Clear existing collection

existing_data = collection.get()

if existing_data["ids"]:
    collection.delete(
        ids=existing_data["ids"]
    )

# Store Chunks in ChromaDB

ids = [f"chunk_{i}" for i in range(len(all_chunks))]

collection.add(
    ids=ids,
    documents=all_chunks,
    embeddings=embeddings.tolist(),
    metadatas=all_metadatas
)

print("\nTotal documents in chromaDB:", collection.count())

# Display Chunks
# for i, chunk in enumerate(chunks, start=1):
#     print(f"\n--- Chunk {i} ---")
#     print(chunk)