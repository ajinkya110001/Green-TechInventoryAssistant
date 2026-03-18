import os
from openai import OpenAI
from fallback import suggest_sustainable

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_ai(item_name):
    if os.getenv("USE_AI") != "true":
        raise Exception("AI unavailable")

    prompt = f"""
    Suggest eco-friendly alternatives for: {item_name}
    Keep it practical and short.
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content


def suggest_fallback(item_name):
    return suggest_sustainable(item_name)