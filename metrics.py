# metrics.py

def avg_usage(history):
    return sum(history) / len(history) if history else 0

def waste_quantity(item):
    usage = avg_usage(item.get("usage_history", []))
    expiry = item.get("expiry_days")

    if usage == 0 or not expiry:
        return 0

    usable_amount = usage * expiry
    remaining = item["quantity"]

    if remaining > usable_amount:
        return remaining - usable_amount  # actual predicted waste

    return 0

def waste_risk_score(item):
    waste = waste_quantity(item)
    qty = item["quantity"]

    if qty == 0:
        return 0

    return round(waste / qty, 2)

def risk_label(score):
    if score > 0.5:
        return "HIGH RISK"
    elif score > 0.2:
        return "MODERATE RISK"
    else:
        return "LOW RISK"


def sustainability_score(inventory):
    total_qty = sum(item["quantity"] for item in inventory)
    waste = total_waste(inventory)

    if total_qty == 0:
        return 100

    score = 100 - (waste / total_qty) * 100
    return round(score, 2)

def explain_waste(item):
    waste = waste_quantity(item)

    if waste == 0:
        return "No waste expected"

    return (
        f"{waste:.2f} units may be wasted because "
        f"consumption rate is lower than stock before expiry."
    )

def total_waste(inventory):
    return sum(waste_quantity(item) for item in inventory)