import os
from openai import OpenAI
from fallback import predict_days_left, expiry_check

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def predict_ai(item):
    if os.getenv("USE_AI") != "true":
        raise Exception("AI unavailable")

    prompt = f"""
    Item: {item['name']}
    Quantity: {item['quantity']}
    Daily usage: {item['daily_usage']}
    Expiry in days: {item.get('expiry_days', 'unknown')}

    Predict:
    1. Days until depletion
    2. Whether it will expire before use
    Keep answer short.
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content


def predict_fallback(item):
    days_left = predict_days_left(item)
    expiry = expiry_check(item)

    if days_left is None:
        return "No usage data available"

    result = f"Will last ~{round(days_left,2)} days"

    if expiry and expiry < days_left:
        result += "May expire before usage"

    return result