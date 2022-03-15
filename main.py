from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# Define your classes variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
MenuItem('name', 'water', 'milk', 'coffee', 'cost')
menu = Menu()
# Boolean variable for the while loop
machine_on = True

while machine_on:
    # a variable for the item options that the coffee produces
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")
    # reports and turns off the machine for maintenance
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        machine_on = False
    else:
        # processes the order taken, checks for available resources and makes the coffee.
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)







