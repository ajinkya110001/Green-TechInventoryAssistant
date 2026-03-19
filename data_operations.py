def add_item(inventory):
    name = input("Item name: ")
    quantity = float(input("Quantity: "))
    expiry = float(input("Expiry days: "))

    history = input("Enter usage history (comma separated): ")
    usage_history = [float(x.strip()) for x in history.split(",") if x.strip()]

    item = {
        "name": name,
        "quantity": quantity,
        "usage_history": usage_history,
        "expiry_days": expiry
    }

    inventory.append(item)
    print("Item added successfully!")
    
def modify_item(inventory):
    for i, item in enumerate(inventory):
        print(f"{i+1}. {item['name']}")

    idx = int(input("Select item to modify: ")) - 1
    item = inventory[idx]

    print("Leave blank to keep existing value")

    new_qty = input(f"Quantity ({item['quantity']}): ")
    new_expiry = input(f"Expiry days ({item.get('expiry_days', 'N/A')}): ")
    new_history = input(f"Usage history ({item.get('usage_history', [])}): ")

    if new_qty:
        item["quantity"] = float(new_qty)

    if new_expiry:
        item["expiry_days"] = float(new_expiry)

    if new_history:
        item["usage_history"] = [
            float(x.strip()) for x in new_history.split(",") if x.strip()
        ]

    print("Item updated!")
    
def add_usage_entry(inventory):
    for i, item in enumerate(inventory):
        print(f"{i+1}. {item['name']}")

    idx = int(input("Select item: ")) - 1
    item = inventory[idx]

    usage = float(input("Enter today's usage: "))

    item.setdefault("usage_history", []).append(usage)

    print("Usage updated!")