def get_base_price(drink, size):
    if drink == "coffee":
        if size == "small":
            return 3
        elif size == "medium":
            return 4
        elif size == "large":
            return 5
    elif drink == "tea":
        if size == "small":
            return 2.5
        elif size == "medium":
            return 3.5
        elif size == "large":
            return 4.5
    elif drink == "smoothie":
        if size == "small":
            return 4
        elif size == "medium":
            return 5
        elif size == "large":
            return 6
    return 0  # fallback for invalid input

def is_valid_drink(drink):
    return drink in ["coffee", "tea", "smoothie"]

def is_valid_size(size):
    return size in ["small", "medium", "large"]

def is_valid_extra(extra):
    return extra in ["milk", "sugar", "syrup"]

def get_extra_price(extra):
    if extra == "milk":
        return 0.5
    elif extra == "sugar":
        return 0.2
    elif extra == "syrup":
        return 0.7
    return 0

print("Welcome to Bean & Brew Cafe!")
grand_total = 0

while True:
    drink = input("\nEnter drink type (Coffee, Tea, Smoothie) or 'done' to finish: ").strip().lower()
    if drink == "done":
        break

    if not is_valid_drink(drink):
        print("Invalid drink type. Please choose Coffee, Tea, or Smoothie.")
        continue

    size = input("Enter size (Small, Medium, Large): ").strip().lower()
    if not is_valid_size(size):
        print("Invalid size. Please choose Small, Medium, or Large.")
        continue

    base_price = get_base_price(drink, size)
    extras_cost = 0
    extras_chosen = []

    if drink != "smoothie":
        while True:
            extra = input("Add an extra (Milk, Sugar, Syrup) or type 'no' to continue: ").strip().lower()
            if extra == "no":
                break
            elif not is_valid_extra(extra):
                print("Invalid extra. Choose from Milk, Sugar, or Syrup.")
                continue
            elif drink == "tea" and extra == "milk":
                print("Milk cannot be added to Tea. Please choose another extra.")
                continue
            else:
                extras_cost += get_extra_price(extra)
                extras_chosen.append(extra)

    total = base_price + extras_cost
    grand_total += total

    print(f"Order Summary: {size.capitalize()} {drink.capitalize()} with {', '.join(extras_chosen) if extras_chosen else 'no extras'} - ${total:.2f}")

print(f"\nGrand Total for your order: ${grand_total:.2f}")
print("Thank you for visiting Bean & Brew Cafe!")