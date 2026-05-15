import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Explain tokens and context window in simple words."
        }
    ]
)

print(response["message"]["content"])