#Day 3 project


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to Treasure Island.\nYour mission is to find the treasure!')
user = input('You are at a crossroad, where do you want to go? Type "left" or "right"\n\t')

if user != 'left' and user!='Left':
    print("Fell into a hole, Game Over...")
else:
    user = input('You turned left, and are now at a lake. Do you swim across, or wait?\n\t')
    if user != 'wait' and user != 'Wait':
        print("Oh no! You were attacked by a trout. Game over.")
    else:
        user = input('By waiting, three doors have magically appeared in front of you! Which door will you take? "Red", "Blue", "Yellow"?\n\t')
        if user == 'red' or user == 'Red':
            print('Burned by fire. Game Over.')
        elif user == 'blue' or user == 'Blue':
            print('Eaten by beasts. Game over.')
        elif user == 'yellow' or user == 'Yellow':
            print('Congratulations. You win!')
        else:
            print('You chose wrong. Game over.')
