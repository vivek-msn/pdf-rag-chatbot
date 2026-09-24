from app.retrieval.retrieval import retrieve_documents
from app.generation.answer_generator import generate_answer


def ask_question(query):

    # Retrieve relevant chunks from ChromaDB
    results = retrieve_documents(query)

    # Extract retrieved documents
    documents = results["documents"][0]

    if not documents:
        return (
            "I don't know based on the provided document.",
            []
        )
    
    # Extract metadata
    metadatas = results['metadatas'][0]

    # Combine retrieved chunks into one context
    context = "\n\n".join(documents)

    # Generate answer using Gemini llm model
    answer = generate_answer(
        query=query,
        context=context
    )

    return answer, metadatas

# Test the complete RAG pipeline

# query = "What is RAG?"
# Interactive chatbot

def run_cli():
    while True:

        query = input("\nYou: ")

        if query.lower() == "exit":
            print("GoodBye!")
            break

        answer, metadatas = ask_question(query)

        print("\nBot:")
        print(answer)

        if metadatas:

            print("\nSources:")

            seen_sources = set()

            for metadata in metadatas:
                source = metadata["source"]
                page = metadata["page"]

                source_key = (source, page)

                if source_key not in seen_sources:
                    print(f"- {source} (Page {page})")
                    seen_sources.add(source_key)


if __name__ == "__main__":
    run_cli()