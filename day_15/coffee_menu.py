from coffee_machine import coffee_machine

def print_menu(): # DONE
    print("What would you like?")
    print("1 ~~ Espresso, $1.50")
    print("2 ~~ Latte, $2.50")
    print("3 ~~ Cappuccino, $3.00")

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
    
def make_coffee(drink_choice): # DONE
    coffee_machine['resources']['water'] -= coffee_machine['flavors'][drink_choice]['water']
    coffee_machine['resources']['milk'] -= coffee_machine['flavors'][drink_choice]['milk']
    coffee_machine['resources']['coffee'] -= coffee_machine['flavors'][drink_choice]['coffee']
    
    print(f'Here is your {drink_choice}. Enjoy!')



def insert_coins(): # DONE
    quarters = int(input('Insert quarters: '))
    dimes = int(input('Insert dimes: '))
    nickels = int(input('Insert nickels: '))
    pennies = int(input('Insert pennies: '))
    customer_total = (quarters*.25)+(dimes*.10)+(nickels*.05)+(pennies*.01)

    print(customer_total)
    return customer_total


def report(): # COMPLETED
    print('Report: ')
    print('\tWater: ' + str(coffee_machine['resources']['water']))
    print('\tMilk: ' + str(coffee_machine['resources']['milk']))
    print('\tCoffee: ' + str(coffee_machine['resources']['coffee']))
    print('\tMoney: ' + str(coffee_machine['resources']['money']))

def sufficient_resources(drink_choice): # COMPLETED
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
options = { # dictionary 
    '1': 'espresso',
    '2': 'latte',
    '3': 'cappuccino',
    'report': 'report',
    'off': 'off',
    'q': 'off'
}
while (user != 'q' and user != 'off'):
    print_menu()
    user = input('Make selection: ')

    drink_choice = options.get(str(user.lower()))
    #print(drink_choice)
    if drink_choice == 'report': report()

    elif drink_choice in coffee_machine['flavors']:
        if sufficient_resources(drink_choice):
            # make drink
            customer_payment = insert_coins()
            transaction_successful = confirm_transaction(customer_payment, drink_choice)

            if transaction_successful:
                make_coffee(drink_choice)

        else:
            print('Please choose another drink')
    
    elif drink_choice not in coffee_machine['flavors']:
        print('Invalid selection.')
        continue
    
print('Goodbye')