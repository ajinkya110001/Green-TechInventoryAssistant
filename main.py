from data_loader import load_json, load_csv, save_csv, save_json
from data_operations import add_item, modify_item, add_usage_entry
from predictor import predict_ai, predict_fallback
from sustainability import suggest_ai, suggest_fallback
from metrics import waste_quantity, waste_risk_score, sustainability_score, explain_waste, risk_label

def main():
    choice = input("Load (1) JSON or (2) CSV? ")

    if choice == "2":
        inventory = load_csv("data/inventory.csv")
    else:
        inventory = load_json("data/inventory.json")

    while True:
        print("\n1. View\n2. Add Item \n3. Modify Item\n4. Add Usage Entry\n5. Predict\n6. Suggest\n7. Waste Report\n8. Save & Commit Changes\n9. Exit")
        c = input("Choice: ")

        if c == "1":
            for item in inventory:
                print(item)
                
        elif c == "2":
            add_item(inventory)
        
        elif c == "3":
            modify_item(inventory)

        elif c == "4":
            add_usage_entry(inventory)

        elif c == "5":
            for item in inventory:
                try:
                    print("\nAI:", predict_ai(item))
                except:
                    print("\nFallback:", predict_fallback(item))

        elif c == "6":
            name = input("Item: ")
            try:
                print("AI:", suggest_ai(name))
            except:
                print("Fallback:", suggest_fallback(name))

        elif c == "7":
            for item in inventory:
                waste = waste_quantity(item)
                score = waste_risk_score(item)
                
                print(f"\nItem: {item['name']}")
                print(f"Waste: {waste}")
                print(f"Risk: {risk_label(score)}")
                print("Why:", explain_waste(item))
            
            print(f"\nOverall Sustainability Score: {sustainability_score(inventory)}%\n")
        elif c == "8":
            save_csv(inventory)
            save_json(inventory)
            print("\nChanges saved!\n")

        else:
            break

if __name__ == "__main__":
    main()