import os
from dotenv import load_dotenv
from google import genai
from app.config import GEMINI_MODEL

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini api key not found.")


# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Generate answer from retrived context
def generate_answer(query, context):


    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I don't know based on the provided document."

Do not use outside knowledge.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text
