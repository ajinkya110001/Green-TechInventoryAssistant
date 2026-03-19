import os
from google import genai
from dotenv import load_dotenv
from fallback import predict_days_left, expiry_check

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
    Keep answer short, the reader should know the context of the answer you are giving.
    """
	try:
		res = client.models.generate_content(
		model="gemini-2.5-flash",
		contents=prompt
		)
		print("AI Prediction successful")
	except Exception as e:
		print("AI Prediction Error:", e)

	return res.text


def predict_fallback(item):
    days_left = predict_days_left(item)
    expiry = expiry_check(item)

    if days_left is None:
        return "No usage data available"

    result = f"Will last ~{round(days_left,2)} days"

    if expiry and expiry < days_left:
        result += "May expire before usage"

    return result