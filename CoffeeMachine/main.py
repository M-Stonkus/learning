MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
Menu = [
    "espresso",
    "latte",
    "cappuccino"
]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

def report_print():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${round(resources["money"],2):.2f}")

def check(selected):
    if resources["water"] < MENU[selected]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["milk"] < MENU[selected]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < MENU[selected]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        money()

def money():
    print("Please insert coins.")
    inserted = (int(input("How many quarters?: ")) * 0.25 +
                int(input("How many dimes?: ")) * 0.1 +
                int(input("How many nickels?: ")) * 0.05 +
                int(input("How many pennies?: ")) * 0.01)
    if inserted < MENU[selection]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] += MENU[selection]["cost"]
        print(f"Here is ${inserted - MENU[selection]['cost']:.2f} dollars in change.")
        make_coffee()

def make_coffee():
    resources["water"] -= MENU[selection]["ingredients"]["water"]
    resources["milk"] -= MENU[selection]["ingredients"]["milk"]
    resources["coffee"] -= MENU[selection]["ingredients"]["coffee"]
    print(f"Here is your {selection}. Enjoy!")

on = True
while on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "off":
        break
    if selection == "report":
        report_print()
    if selection in Menu:
        check(selection)


