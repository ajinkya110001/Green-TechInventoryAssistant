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
    Keep it practical and short. Dont use * in your response.
    """

    res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
	)

    return res.text


def suggest_fallback(item_name):
    return suggest_sustainable(item_name)

def suggest_suppliers_ai(item_name):
    """Suggest local, fair-trade suppliers for an item"""
    if os.getenv("USE_AI") != "true":
        raise Exception("AI unavailable")

    prompt = f"""
    Suggest 2-3 local, fair-trade suppliers or alternatives for: {item_name}
    Be specific with supplier names or types.
    Keep it concise. Don't use * in your response.
    """

    try:
        res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return res.text
    except Exception as e:
        return f"Supplier suggestion error: {e}"