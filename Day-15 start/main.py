#TODO : 2. check resource sufficient to  make drink order.

MENU = {
    "espresso": {
        "intgredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
        "latte": {
            "intgredients":{
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "Cost": 2.5,
        },

            "cappuccino" : {
                "intgredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee":24,
                },
                "cost": 3.0,
            }
               }

profit =0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#TODO: 1. print report of all coffee machine resource

def is_resource_suffieceint(order_intgredients):
    """ returns True when corder can be made, False if intgredients are insufficent."""
    for item in order_intgredients:
       if order_intgredients[item] >= resources[item]:
        print(f"sorry  there is not enough water{item}.")
        return  False
    return False

def is_transaction_Seccessfull(money_recieved, drink_cost):
    """:returns true when payment is accepted , or false if money is insuffiecient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here is {change} in chane.")
        global  profit
        profit += drink_cost
        return  True
    else:
        print("sorry that's enough money, money refunded")
        return  False
def process_coins():
    """returns the total"""
    print("please insert coins.")
    total = int(input("how many quaters?  ")) * 0.25
    total += int(input("how many dimes?  ")) * 0.1
    total += int(input("how many nickles?  ")) * 0.05
    total += int(input("how many pennies?  ")) * 0.01
    return  total

iso_on = True
while iso_on:
        choice = input("what would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
         iso_on = False
        elif choice == "report":
         print(f"printwater:180ml")
        print(f"milk: {resources['water']}ml")
        print(f"coffee: {resources['milk']}g")
        print(f"money: $ {resources['coffee']}g")
        print(f"money : ${profit}")
else:
    drink = MENU[choice]
    if is_resource_suffieceint(drink["intgredients"]) :
           payment = process_coins()
           is_transaction_Seccessfull(payment, drink["cost"])




