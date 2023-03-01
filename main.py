from data import MENU
from data import resources


# GLOBAL VARIABLES
QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

COST_ESPRESSO = 1.50
COST_LATTE = 2.50
COST_CAPPUCCINO = 3.00


# FUNCTIONS
def count_money(q, d, n, p):
    return QUARTER*q + DIME*d + NICKLE*n + PENNY*p


# make a function to print report
def report(collection):
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"Money: ${collection}")


# make a function to check if the resources are sufficient
def check_resources(req_water, req_coffee, req_milk):
    if resources["water"] < req_water:
        return "no water"
    elif resources["coffee"] < req_coffee:
        return "no coffee"
    elif resources["milk"] < req_milk:
        return "no milk"
    else:
        return "resources available"


# make coffe and use the resources required for it
def make_coffee(req_water, req_coffee, req_milk):
    resources["water"] = resources["water"] - req_water
    resources["coffee"] = resources["coffee"] - req_coffee
    resources["milk"] = resources["milk"] - req_milk


def espresso():
    water = MENU["espresso"]["ingredients"]["water"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    milk = 0

    is_available = check_resources(water, coffee, milk)

    if is_available == "resources available":
        make_coffee(water, coffee, milk)
        return "here is your espresso"
    else:
        return is_available


def latte():
    water = MENU["latte"]["ingredients"]["water"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    milk = MENU["latte"]["ingredients"]["milk"]

    is_available = check_resources(water, coffee, milk)

    if is_available == "resources available":
        make_coffee(water, coffee, milk)
        return "here is your latte"
    else:
        return is_available


def cappuccino():
    water = MENU["cappuccino"]["ingredients"]["water"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]

    is_available = check_resources(water, coffee, milk)

    if is_available == "resources available":
        make_coffee(water, coffee, milk)
        return "here is your cappuccino"
    else:
        return is_available


# make a function to process coins and return the money
def calculate_change(amt_inserted, coff_type, money, coff_cost, what_coff):
    ans = coff_type
    if ans == f"here is your {what_coff}":
        money += coff_cost
        amount_left = round(amt_inserted - coff_cost, 2)
        # return the change to the user
        print(f"here is your {what_coff}")
        print(f"Here is ${amount_left} in change.")
    else:
        print(f"{ans}, money refunded")
    return money


# WORKING

def coffee_machine():
    money = 0
    want_coffee = True

    while want_coffee:
        # print the prompt asking user what they want and ask them to insert coins
        coff = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coff == "report":
            report(money)
        # turn off the machine with the off prompt
        elif coff == "off":
            want_coffee = False
            print(resources["water"])
        else:
            print("Please insert coins")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))

            amount_inserted = count_money(quarters, dimes, nickles, pennies)

            if coff == "espresso":
                if amount_inserted >= COST_ESPRESSO:
                    money = calculate_change(amount_inserted, espresso(), money, COST_ESPRESSO, "espresso")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            elif coff == "latte":
                if amount_inserted >= COST_LATTE:
                    money = calculate_change(amount_inserted, latte(), money, COST_LATTE, "latte")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            elif coff == "cappuccino":
                if amount_inserted >= COST_CAPPUCCINO:
                    money = calculate_change(amount_inserted, cappuccino(), money, COST_CAPPUCCINO, "cappuccino")
                else:
                    print("Sorry that's not enough money. Money refunded.")


coffee_machine()
