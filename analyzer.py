import os
from openai import OpenAI

# Get API key safely
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Set OPENAI_API_KEY in Streamlit secrets.")

# Create client
client = OpenAI(api_key=api_key)

def analyze(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
