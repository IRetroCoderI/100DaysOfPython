from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create instances of Menu, CoffeeMaker, and MoneyMachine Objs
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user = ''
while (user != 'q' and user != 'quit'): 
    print(menu.get_items())
    
    for item in menu.menu:
        print(f"{item.name}: ${item.cost}")
    user = input('Make selection please: ')

    if user == 'report': 
        coffee_maker.report()
        money_machine.report()
    elif (user == 'q' or user == 'quit'): continue 
    else: 
        item = menu.find_drink(user) # if item in menu, cont
        # now that we have item, check if suff. resources
        can_make = coffee_maker.is_resource_sufficient(item)

        if money_machine.make_payment(item.cost):
            # give customer their drink of choice
            coffee_maker.make_coffee(item)        
        else:
            continue

    

    
    