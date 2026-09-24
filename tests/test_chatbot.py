from app import chatbot


def test_ask_question_returns_answer_and_sources(monkeypatch):

    fake_results = {
        "documents": [["RAG is Retrieval-Augmented Generation."]],
        "metadatas": [[
            {
                "source": "data/rag_guide.pdf",
                "page": 1
            }
        ]],
        "distances": [[0.5]]
    }

    monkeypatch.setattr(
        chatbot,
        "retrieve_documents",
        lambda query: fake_results
    )

    monkeypatch.setattr(
        chatbot,
        "generate_answer",
        lambda query, context: "RAG answer"
    )

    answer, metadatas = chatbot.ask_question(
        "What is RAG?"
    )

    assert answer == "RAG answer"
    assert metadatas == fake_results["metadatas"][0]



def test_ask_question_fallback_when_no_documents(monkeypatch):

    fake_results = {
        "documents": [[]],
        "metadatas": [[]],
        "distances": [[]]
    }

    monkeypatch.setattr(
        chatbot,
        "retrieve_documents",
        lambda query: fake_results
    )

    answer, metadatas = chatbot.ask_question(
        "What is the capital of Japan?"
    )

    assert answer == "I don't know based on the provided document."
    assert metadatas == []