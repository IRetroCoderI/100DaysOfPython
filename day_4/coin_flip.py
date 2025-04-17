# day 4 - radomisation and lists
import random

def flip_coin():
    coin = ['tails', 'heads']
    side = coin[random.randint(0,1)]
    print(side)

flip_coin()
flip_coin()
flip_coin()