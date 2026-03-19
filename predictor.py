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
    Daily usage: {item['usage_history']}
    Expiry in days: {item.get('expiry_days', 'unknown')}

    Predict:
    1. Days until depletion
    2. Whether it will expire before use
    Keep answer short, the reader should know the context of the answer you are giving. Dont use * in your response.
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

def predict_bulk_depletion(inventory):
	"""Analyze entire inventory and identify items depleting before expiry"""
	if os.getenv("USE_AI") != "true":
		raise Exception("AI unavailable")

	prompt = f"""
	Analyze this inventory data and identify items that will DEPLETE (run out) before they EXPIRE.

	Inventory:
	{inventory}

	For each item (dont print this in response, just use it for your analysis):
	- Calculate: Days until depletion = quantity / daily_usage (average from usage_history)
	- Compare with: expiry_days
	- If days_until_depletion < expiry_days, the item will deplete before expiry
	- If expiry_days < days_until_depletion, the item will EXPIRE before depletion

	Return ONLY a list of item names that will DEPLETE BEFORE EXPIRY.
	Format: "Item1, Item2, Item3"
	Also give an optimal quantity suggestion for each at-risk item based on usage and expiry to minimize waste.
	If no items at risk, return "No items at risk - all items will deplete before expiry"
	Dont use * in your response.
	"""

	try:
		res = client.models.generate_content(
			model="gemini-2.5-flash",
			contents=prompt
		)
		print("Bulk depletion analysis successful")
		return res.text
	except Exception as e:
		print("Bulk depletion analysis error:", e)
		return str(e)

def analyze_waste_report_ai(inventory, waste_data):
	"""AI analysis of waste report for strategic insights"""
	if os.getenv("USE_AI") != "true":
		raise Exception("AI unavailable")

	prompt = f"""
	Analyze this inventory waste report and provide strategic insights:

	Inventory Waste Data:
	{waste_data}

	Provide:
	1. Key patterns (e.g., overordering, seasonal trends)
	2. Top 3 items at highest waste risk
	3. Priority actions

	Keep it strictly concise and actionable which is understandable to a layperson. Dont use * in your response.
	"""

	try:
		res = client.models.generate_content(
			model="gemini-2.5-flash",
			contents=prompt
		)
		return res.text
	except Exception as e:
		raise Exception(f"Waste analysis error: {e}")