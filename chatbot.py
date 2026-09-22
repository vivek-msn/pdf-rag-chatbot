from retrieval import retrieve_documents
from answer_generator import generate_answer


def ask_question(query):

    # Retrieve relevant chunks from ChromaDB
    results = retrieve_documents(query)

    # Extract retrieved documents
    documents = results["documents"][0]

    # Combine retrieved chunks into one context
    context = "\n\n".join(documents)

    # Generate answer using Gemini llm model
    answer = generate_answer(
        query=query,
        context=context
    )

    return answer

# Test the complete RAG pipeline

query = "What is RAG?"

answer = ask_question(query)

print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)