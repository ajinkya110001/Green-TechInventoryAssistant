# fallback.py

def predict_days_left(item):
    if item["daily_usage"] == 0:
        return None
    return item["quantity"] / item["daily_usage"]


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


def suggest_sustainable(item_name):
    db = sustainability_db()
    return db.get(item_name.lower(), "Consider reusable or eco-friendly alternatives")