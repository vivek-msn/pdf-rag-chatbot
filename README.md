# PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) application that processes PDF documents, creates semantic embeddings, stores them in ChromaDB, and retrieves relevant document chunks for question answering.

## 🚧 Project Status

Currently implementing the core PDF ingestion and retrieval pipeline.

### Completed

- PDF text extraction
- Recursive text chunking
- Sentence Transformer embeddings
- ChromaDB vector storage

### Upcoming

- Semantic retrieval
- Gemini-powered answer generation
- End-to-end chatbot
- FastAPI backend
- Frontend interface
- Dockerization
- Deployment

---

## 🏗️ RAG Architecture

```text
PDF Document
     ↓
Text Extraction
     ↓
Recursive Chunking
     ↓
Sentence Transformer Embeddings
     ↓
ChromaDB
     ↓
Semantic Retrieval
     ↓
Gemini
     ↓
Grounded Answer