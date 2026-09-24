# PDF Configuration

PDF_PATH = "data/rag_guide.pdf"

# Chunking Configuration

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Embedding Configuration

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ChromaDB Configuration

CHROMA_DB_PATH = "pdf_chroma_db"
COLLECTION_NAME = "pdf_documents"

# Retrieval Configuration

TOP_K = 3
DISTANCE_THRESHOLD = 1.5

# LLM Configuration

GEMINI_MODEL = "gemini-3.1-flash-lite"