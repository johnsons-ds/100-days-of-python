from menu import MENU
from menu import resources

profit = 0

is_on = True

def check_resources(order):
    """Returns true if there are available resources to make the coffee. Otherwise it returns false and prompts the user that their coffee cannot be made."""
    for i in order:
       if order[i] >= resources[i]:
           print(f"Sorry there is not enough {i}.")
           return False
    return True


def coins_inserted():
    """ Returns the total value amount from the coins inserted by the user"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(money_provided, drink_cost):
    """Return true when the payment is accepted or false if there is not enough money."""
    global profit
    if money_provided >= drink_cost:
        change = round(money_provided - drink_cost, 2)
        print(f"Here is {change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """This function deduct the required ingredients from the resources."""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name} ☕️")



while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = coins_inserted()
            if transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
