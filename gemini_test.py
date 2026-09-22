import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini api key not found.")

client = genai.Client(api_key=api_key)

# print("Gemini client initialized successfully.")

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="What is RAG? Explain in one sentence."
)

print("\nGemini Response:")
print(response.text)