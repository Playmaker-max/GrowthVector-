import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    max_retries=4
)

MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")


def analyze_property(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are GrowthVector's Property Intelligence Engine. "
                    "Analyze real-estate properties and marketing information "
                    "carefully. Separate verified facts from hypotheses."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
        max_tokens=int(os.getenv("GROQ_MAX_TOKENS", "4500")),
    )

    return response.choices[0].message.content
