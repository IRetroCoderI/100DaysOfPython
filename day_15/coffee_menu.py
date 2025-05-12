from coffee_machine import coffee_machine

def print_menu(): 
    print("What would you like?")
    print("1 ~~ Espresso")
    print("2 ~~ Latte")
    print("3 ~~ Cappuccino")

def confirm_transaction(customer_payment, drink_choice):
    coffee_price = coffee_machine['flavors'][drink_choice]['price']

    if customer_payment < coffee_price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        # calculate change if any
        if customer_payment > coffee_price:
            change = customer_payment - coffee_price
            print(f"Your change is ${change:.2f}")

        coffee_machine['resources']['money'] += coffee_price
        return True
    
def make_coffee(drink_choice):
    coffee_machine['resources']['water'] -= coffee_machine['flavors'][drink_choice]['water']
    coffee_machine['resources']['milk'] -= coffee_machine['flavors'][drink_choice]['milk']
    coffee_machine['resources']['coffee'] -= coffee_machine['flavors'][drink_choice]['coffee']
    
    print(f'Here is your {drink_choice}. Enjoy!')



def insert_coins():
    quarters = int(input('Insert quarters: '))
    dimes = int(input('Insert dimes: '))
    nickels = int(input('Insert nickels: '))
    pennies = int(input('Insert pennies: '))
    customer_total = (quarters*.25)+(dimes*.10)+(nickels*.05)+(pennies*.01)

    print(customer_total)
    return customer_total


def report():
    print('Report: ')
    print('\tWater: ' + str(coffee_machine['resources']['water']))
    print('\tMilk: ' + str(coffee_machine['resources']['milk']))
    print('\tCoffee: ' + str(coffee_machine['resources']['coffee']))
    print('\tMoney: ' + str(coffee_machine['resources']['money']))

def sufficient_resources(drink_choice):
    # check water
    # check milk
    # check coffee
    if coffee_machine['resources']['coffee'] < coffee_machine['flavors'][drink_choice]['coffee']:
        print('not enough coffee')
        return False
    elif coffee_machine['resources']['water'] < coffee_machine['flavors'][drink_choice]['water']:
        print('not enough water')
        return False
    elif coffee_machine['resources']['milk'] < coffee_machine['flavors'][drink_choice]['milk']:
        print('not enough milk')
        return False
    else:
        return True

user = ''
while (user != 'q' and user != 'off'):
    print_menu()
    user = input('Make selection: ')
    # TODO: have users input tied to string so they don't have to type the whole flavor choice
    drink_choice = user

    if user == 'report': report()

    elif sufficient_resources(drink_choice):
        # make drink
        customer_payment = insert_coins()
        transaction_successful = confirm_transaction(customer_payment, drink_choice)

        if transaction_successful:
            make_coffee(drink_choice)

    else:
        print('choose another drink buddy')
    
print('goodbye')