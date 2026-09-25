from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_home():

     response = client.get("/")

     assert response.status_code == 200

     assert response.json() == {
          "message": "RAG API is running"
     }


def test_ask():

     response = client.post(
          "/ask",
          json={
               "question": "What is RAG?"
          }
     )

     assert response.status_code == 200

     data = response.json()

     assert "answer" in data
     assert "sources" in data


def test_ask_validation_error():

    response = client.post(
         "/ask",
         json={
              "question": ""
         }
    )

    assert response.status_code == 422