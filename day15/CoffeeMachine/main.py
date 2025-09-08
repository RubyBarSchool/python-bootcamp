from resource import *

def prompt_asking():
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid choice. Please select again.")
        return prompt_asking()
    else:
        return choice

def print_report():
    for key, value in RESOURCE.items():
        print(f"{key}: {value['quantity']}{value['unit']}")

def check_resources(choice):
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        if ingredients[item] > RESOURCE[item]["quantity"]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins(choice):
    if RESOURCE["Money"]["quantity"] < MENU[choice]["cost"]:
        print("Please insert coins.")
        total = 0
        for coin, value in COIN.items():
            count = int(input(f"How many {coin}?: "))
            total += count * value
        total += RESOURCE["Money"]["quantity"]
        total = round(total, 2)
        print(f"Here is ${total} in change")
        return total
    return RESOURCE["Money"]["quantity"]

def check_transaction(payment, cost):
    if payment < cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        return True


def make_coffee(choice, payment, cost):
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        RESOURCE[item]["quantity"] -= ingredients[item]
    RESOURCE["Money"]["quantity"] = round(payment - cost, 2)
    print(f"Here is your {choice}. Enjoy!")

def order():
    choice = prompt_asking()
    if choice == "report":
        print_report()
    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins(choice)
            if check_transaction(payment, MENU[choice]["cost"]):
                make_coffee(choice, payment, MENU[choice]["cost"])
    else:
        print("Invalid choice. Please select again.")

    return choice

def main():
    choice = None
    while "off" != choice:
        choice = order()


if __name__ == "__main__":
    main()