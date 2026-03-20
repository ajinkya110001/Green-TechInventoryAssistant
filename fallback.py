
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
    depleted_before_expiry = []

    for item in inventory:
        waste = waste_quantity(item)
        if waste == 0:
            depleted_before_expiry.append(item['name'])

    if not depleted_before_expiry:
        return "No items deplete before expiry - all items have waste risk"

    return ", ".join(depleted_before_expiry)


def suggest_sustainable(item_name):
    db = sustainability_db()
    return db.get(item_name.lower(), "Consider reusable or eco-friendly alternatives")