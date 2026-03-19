# fallback.py
from metrics import waste_quantity

def avg_usage(history):
    return sum(history) / len(history) if history else 0

def predict_days_left(item):
    usage = avg_usage(item.get("usage_history", []))

    if usage == 0:
        return None

    return item["quantity"] / usage


def expiry_check(item):
    # simple expiry logic (days remaining)
    expiry_days = item.get("expiry_days", None)
    return expiry_days


def sustainability_db():
    return {
        "plastic bottles": "Use reusable steel bottles",
        "paper cups": "Switch to ceramic/reusable cups",
        "coffee beans": "Buy fair-trade or locally sourced coffee",
        "packaged snacks": "Buy in bulk to reduce packaging"
    }
    
def predict_bulk_depletion_fallback(inventory):
    """Fallback: Identify items depleting before expiry using calculations"""
    at_risk = []
    
    for item in inventory:
        waste = waste_quantity(item)
        if waste > 0:
            at_risk.append(item['name'])
    
    if not at_risk:
        return "No items at risk - all items will deplete before expiry"
    
    return ", ".join(at_risk)


def suggest_sustainable(item_name):
    db = sustainability_db()
    return db.get(item_name.lower(), "Consider reusable or eco-friendly alternatives")