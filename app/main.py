import re

from app.groq import analyze_property as call_groq
from app.schemas import PropertyIntelligence


def _extract_json(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model output")
    return text[start : end + 1]


def analyze_property(listing: str) -> PropertyIntelligence:
    prompt = f"""
Analyze the property listing below for a real-estate agent.
Base facts only on the listing. Fill every field in the schema.
Keep the JSON compact: at most 5 verified_facts, 4 missing_information, 2 buyer_hypotheses, 3 marketing_opportunities and 3 campaign_angles. Keep every string under 25 words. Make the description about 70 words.
For listing_copy, write a headline, a description of about 100 words and a short social post. Use only facts stated in the listing. Do not invent features, views, distances or school names. Do not use unverifiable claims such as 'sought-after', 'prime location', 'perfect for' or 'ideal for'. State only what the listing says.
The listing is South African. In missing_information and next_best_action, consider what an agent would need before a sale: compliance certificates, approval status of any extra structures such as staff quarters, and the age or condition of installed items like geysers, pools and roofs. Tie next_best_action to this specific listing.

Return ONLY valid JSON matching this structure:
{PropertyIntelligence.model_json_schema()}

LISTING:
{listing}
"""
    raw = call_groq(prompt)
    return PropertyIntelligence.model_validate_json(_extract_json(raw))


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
