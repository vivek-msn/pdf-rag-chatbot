# PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) application that processes PDF documents, creates semantic embeddings, stores them in ChromaDB, and retrieves relevant document chunks for question answering.

## 🚧 Project Status

Core RAG pipeline, FastAPI backend, and frontend interface are complete.

### Completed

- PDF text extraction
- Recursive text chunking
- Sentence Transformer embeddings
- ChromaDB vector storage
- Semantic retrieval
- Gemini-powered answer generation
- FastAPI backend
- Frontend chat interface
- Source display
- Loading and error handling
- API validation and testing
- FastAPI-based frontend serving

### Next Steps

- Final documentation and cleanup
- Dockerization
- Deployment

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
Relevant Chunks
     ↓
Gemini
     ↓
Grounded Answer
     ↓
FastAPI Response
     ↓
Frontend Chat UI


## 🛠️ Tech Stack

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- Google Gemini
- Pydantic
- HTML
- CSS
- JavaScript
- Pytest


## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vivek-msn/pdf-rag-chatbot.git
cd pdf-rag-chatbot


## 📁 Project Structure

```text
pdf-rag-chatbot/
│
├── app/
│   ├── generation/
│   │   ├── __init__.py
│   │   └── answer_generator.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   └── pdf_loader.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   └── retrieval.py
│   │
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   └── main.py
│
├── data/
│   └── rag_guide.pdf
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   ├── test_chatbot.py
│   └── test_main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


## 🔄 How It Works

1. The application loads text from the PDF document.
2. The extracted text is split into smaller chunks using recursive text splitting.
3. Each chunk is converted into a vector embedding using Sentence Transformers.
4. The embeddings and document metadata are stored in ChromaDB.
5. When a user asks a question, the question is converted into an embedding.
6. ChromaDB retrieves the most relevant document chunks.
7. The retrieved context is passed to Google Gemini.
8. Gemini generates an answer based on the retrieved context.
9. FastAPI returns the answer along with source metadata.
10. The frontend displays the answer and document sources to the user.

## 🧪 Testing

The project includes automated tests for the RAG chatbot and FastAPI API.

Run the test suite:

```bash
python -m pytest