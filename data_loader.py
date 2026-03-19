import csv
import json

def load_json(path):
    with open(path) as f:
        return json.load(f)


def load_csv(path):
    data = []

    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            usage_history = [
                float(x.strip()) for x in row["usage_history"].split(",") if x.strip()
            ]

            data.append({
                "name": row["name"],
                "quantity": float(row["quantity"]),
                "usage_history": usage_history,
                "expiry_days": float(row["expiry_days"])
            })

    return data

def save_csv(inventory):
    with open("data/inventory.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "quantity", "daily_usage", "expiry_days"]
        )
        writer.writeheader()

        for item in inventory:
            writer.writerow({
                "name": item["name"],
                "quantity": item["quantity"],
                "daily_usage": item["daily_usage"],
                "expiry_days": item.get("expiry_days", "")
            })


def save_json(inventory):
    with open("data/inventory.json", "w") as f:
        json.dump(inventory, f, indent=2)