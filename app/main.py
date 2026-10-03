import os
from dotenv import load_dotenv
from google import genai
from app.schemas import PropertyIntelligence

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-3.8-flash"

def analyze_property(listing: str):
    prompt = f"""
You are GrowthVector Property Intelligence.

Analyze the property listing below.

Return ONLY valid JSON matching this structure:
{PropertyIntelligence.model_json_schema()}

LISTING:
{listing}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )

    return PropertyIntelligence.model_validate_json(response.text)

if __name__ == "__main__":
    listing = """
3-bedroom townhouse in Greenstone Hill, Edenvale.
Price: R1,650,000.
104 m² ground-floor unit with private garden.
Modern kitchen, gas stove, secure complex, 24/7 security and pet-friendly.
Close to major roads, shopping centres and schools.
"""

    result = analyze_property(listing)
    print(result.model_dump_json(indent=2))
