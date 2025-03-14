import logging
import ollama

logging.basicConfig(level=logging.INFO)
logging.info("Using LLaMA 3 from Ollama...")

def process_query_with_llama(query: str, max_length: int = 100) -> str:
    try:
        # Generate a response using Ollama's LLaMA 3
        response = ollama.chat(
            model="llama3",  # Use the local LLaMA 3 model in Ollama
            messages=[{"role": "user", "content": query}]
        )

        # Extract and return the generated text
        return response["message"]["content"]
    except Exception as e:
        logging.error("Error processing query with LLaMA 3: %s", e)
        return "Error processing query."
