import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv() 

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("❌ OPENROUTER_API_KEY not found in environment!")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def generate_response(prompt_text):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Respond clearly and completely, but stay under 200 words."
                },
                {
                    "role": "user",
                    "content": [{"type": "text", "text": prompt_text}]
                }
            ],
            max_tokens=300,
            extra_headers={
                "HTTP-Referer": "https://yourdomain.com",
                "X-Title": "AffiliateBot",
            },
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
