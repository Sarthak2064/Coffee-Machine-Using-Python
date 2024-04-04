MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.00
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.00
    }
}

profit = 0
resources = {
    "water": 400,
    "coffee": 100,
    "milk": 200,
}


def is_resource_available(req_ingredients):
    for item in req_ingredients:
        if req_ingredients[item] > resources[item]:
            print(f"Sorry, there are not enough ${item}")
            return False
    return True


def process_coins():
    print("Please Insert Coins :")
    total = int(input("No. Of Quarters : ")) * 0.25
    total += int(input("No. Of Dimes : ")) * 0.1
    total += int(input("No. Of Nickles : ")) * 0.05
    total += int(input("No. Of Pennies : ")) * 0.01
    return total


def transaction(u_payment, drink_cost):
    if u_payment >= drink_cost:
        change = round(u_payment - drink_cost, 2)
        print(f"Here's your change ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry Not Enough Money, Transaction Failed")
        return False


def make_drink(order, req_ingredients):
    for item in req_ingredients:
        resources[item] -= req_ingredients[item]
    print(f"Here's your {order}, Thank you.")


is_on = True

while is_on:
    choice = input("Enter Your Choice(espresso/latte/cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_available(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
