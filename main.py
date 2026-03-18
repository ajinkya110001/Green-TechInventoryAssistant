from data_loader import load_json, load_csv
from predictor import predict_ai, predict_fallback
from sustainability import suggest_ai, suggest_fallback
from metrics import total_waste

def main():
    choice = input("Load (1) JSON or (2) CSV? ")

    if choice == "2":
        inventory = load_csv("data/inventory.csv")
    else:
        inventory = load_json("data/inventory.json")

    while True:
        print("\n1. View\n2. Predict\n3. Suggest\n4. Waste Report\n5. Exit")
        c = input("Choice: ")

        if c == "1":
            for item in inventory:
                print(item)

        elif c == "2":
            for item in inventory:
                try:
                    print("\nAI:", predict_ai(item))
                except:
                    print("\nFallback:", predict_fallback(item))

        elif c == "3":
            name = input("Item: ")
            try:
                print("AI:", suggest_ai(name))
            except:
                print("Fallback:", suggest_fallback(name))

        elif c == "4":
            waste = total_waste(inventory)
            print(f"Estimated waste risk: {waste}")

        else:
            break

if __name__ == "__main__":
    main()