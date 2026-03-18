# metrics.py

def waste_risk(item):
    if item["daily_usage"] == 0:
        return 0

    days_left = item["quantity"] / item["daily_usage"]
    expiry = item.get("expiry_days", None)

    if expiry and expiry < days_left:
        return item["quantity"] * 0.5  # assume 50% waste

    return 0


def total_waste(inventory):
    return sum(waste_risk(item) for item in inventory)