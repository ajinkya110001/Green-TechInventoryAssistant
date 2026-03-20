from data_loader import load_json, load_csv, save_csv, save_json
from data_operations import add_item, modify_item, add_usage_entry, delete_item
from predictor import predict_ai, predict_fallback, predict_bulk_depletion, analyze_waste_report_ai
from sustainability import suggest_ai, suggest_fallback
from metrics import waste_quantity, waste_risk_score, sustainability_score, explain_waste, risk_label, restock_suggestion
from fallback import predict_bulk_depletion_fallback

def main():
    # choice = input("Load (1) JSON or (2) CSV? ")
    print("Loading inventory data from JSON...\n\n")

#####loading json only for now, can change to csv also if needed, as data opreations would be donr in csv as well#####
    # if choice == "2":
    #     inventory = load_csv("data/inventory.csv")
    # else:
    inventory = load_json("data/inventory.json")

    while True:
        print("\n1. View Item(s)\n2. Add Item\n3. Modify Item\n4. Delete Item\n5. Add Usage Entry\n6. Predict depletion/wastage\n7. Suggest other options\n8. Waste Report\n9. Save/Commit Changes & Exit")
        c = input("Choice: ")

        if c == "1":
            item=input("Enter item name to view (or press Enter to view all): ").strip().lower()
            for i in inventory:
                if item == "" or item in i["name"].lower():
                    print(i)
            try:
                result = predict_bulk_depletion(inventory)
                print("\n ITEMS AT RISK OF EXPIRING BEFORE DEPLETION:\n")
                print(result)
            except Exception as e:
                print(f"Error in bulk analysis: {e}")
                print("\nGOING FOR FALLBACK ...\n")
                print(predict_bulk_depletion_fallback(inventory))
            
        elif c == "2":
            add_item(inventory)
        
        elif c == "3":
            modify_item(inventory)

        elif c == "4":
            delete_item(inventory)

        elif c == "5":
            add_usage_entry(inventory)

        elif c == "6":
            while True:
                item_name = input("\nWhich item to predict for? (or 'back' to return to menu): ").strip().lower()

                if item_name == "back":
                    break

                # Search for item in inventory
                found_item = None
                for item in inventory:
                    if item["name"].lower() == item_name:
                        found_item = item
                        break

                if not found_item:
                    print(f"\n Item '{item_name}' not found in inventory.")
                    retry = input("Try again? (yes/no): ").strip().lower()
                    if retry != "yes":
                        break
                    continue

                # Item found, predict
                print("= " * 50)
                print(f"\nPredicting for {found_item['name']}...")
                print("= " * 50)
                try:
                    print("\nAI:", predict_ai(found_item))
                except Exception as e:
                    print("\nFallback:", predict_fallback(found_item))

                break

        elif c == "7":
            name = input("Please provide the item name for which you want suggestions: ")
            try:
                print("AI:", suggest_ai(name))
            except Exception as e:
                print(f"Error occurred: {e}")
                print("Fallback:", suggest_fallback(name))

        elif c == "8":
            # First, show basic waste metrics
            waste_data = []
            for item in inventory:
                waste = waste_quantity(item)
                score = waste_risk_score(item)

                print(f"\nItem: {item['name']}")
                print(f"Current Quantity: {item['quantity']}")
                print(f"Waste: {waste}")
                print(f"Risk: {risk_label(score)}")
                print("Why:", explain_waste(item))

                # Collect data for AI analysis
                waste_data.append({
                    "name": item['name'],
                    "quantity": item['quantity'],
                    "waste": waste,
                    "risk": risk_label(score),
                    "explanation": explain_waste(item)
                })

            print(f"\nOverall Sustainability Score: {sustainability_score(inventory)}%\n")

            # Then, try to get AI insights
            print("=" * 50)
            print(" AI WASTE ANALYSIS & RECOMMENDATIONS")
            print("=" * 50)
            try:
                insights = analyze_waste_report_ai(inventory, waste_data)
                print(insights)
            except Exception as e:
                print(f"AI analysis unavailable: {e}")
                print("\n(Showing basic metrics only - upgrade to enable AI insights)\n")
        else:
            save_csv(inventory)
            save_json(inventory)
            print("\nChanges saved!\n")
            print("Exiting...\n")

if __name__ == "__main__":
    main()