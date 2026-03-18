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
            data.append({
                "name": row["name"],
                "quantity": float(row["quantity"]),
                "daily_usage": float(row["daily_usage"]),
                "expiry_days": float(row["expiry_days"])
            })
    return data