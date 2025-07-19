from openai import OpenAI

# Point to your vLLM server
client = OpenAI(
    api_key="token-abc123",
    base_url="http://localhost:8000/v1"
)

# Test chat completion
response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {"role": "user", "content": "What are SEC filings and why are they important?"}
    ],
    max_tokens=200,
    temperature=0.1
)

print(response.choices[0].message.content)
