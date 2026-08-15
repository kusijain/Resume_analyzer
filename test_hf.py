import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_key)

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Summarize this in one sentence: I am a Python developer with 3 years of experience."}
        ],
        max_tokens=50,
    )
    print("SUCCESS:")
    print(response.choices[0].message.content)
except Exception as e:
    print("ERROR:")
    print(e)