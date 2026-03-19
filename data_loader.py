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
                int(x.strip()) for x in row["usage_history"].split(",") if x.strip()
            ]

            data.append({
                "name": row["name"],
                "quantity": int(row["quantity"]),
                "usage_history": usage_history,
                "expiry_days": int(row["expiry_days"])
            })

    return data

def save_csv(inventory):
    with open("data/inventory.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "quantity", "usage_history", "expiry_days"]
        )
        writer.writeheader()

        for item in inventory:
            writer.writerow({
                "name": item["name"],
                "quantity": item["quantity"],
                "usage_history": ", ".join(str(x) for x in item["usage_history"]),
                "expiry_days": item.get("expiry_days", "")
            })


def save_json(inventory):
    with open("data/inventory.json", "w") as f:
        json.dump(inventory, f, indent=2)