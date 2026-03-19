import os
from dotenv import load_dotenv
from google import genai
from fallback import suggest_sustainable

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def suggest_ai(item_name):
    if os.getenv("USE_AI") != "true":
        raise Exception("AI unavailable")

    prompt = f"""
    Suggest eco-friendly alternatives for: {item_name}
    Keep it practical and short.
    """

    res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
	)

    return res.text


def suggest_fallback(item_name):
    return suggest_sustainable(item_name)