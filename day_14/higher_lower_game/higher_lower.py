from data import data_list
from art import *
import os
import random

# data_list[i] = indexes each entry with (username, name, followers, profession, and country)
# print(data_list[0]['country']) 

# create while loop
# select a and b for game
# if correct, set correct option as a and choose new b, ask user to choose again
# if false, player loses, display score, then play again?

def reveal_followers(a, b):
    print("\n")
    print(f"{a['name']}, {a['profession']}: {a['followers']} million followers")
    print(f"{b['name']}, {b['profession']}: {b['followers']} million followers")


def check_answer(a, b, user):
    higher_follower = a if float(a['followers']) >= float(b['followers']) else b

    if user in str(higher_follower['name']):
        print("~~~~CORRECT~~~~")
        reveal_followers(a,b)
        res = True
    else:
        print("~~~~WRONG!~~~~")
        #print(f"correct: {higher_follower['followers']}")
        reveal_followers(a,b)
        res = False
    return res


active = True
while (active) :
    a = random.choice(data_list) # select person a
    b = random.choice(data_list) # select person b
    #higher_follower = a if a['followers'] > b['followers'] else b

    user = input(f"Who has more followers?...\n\n {a['name']}, {a['profession']}\n\tOR\n {b['name']}, {b['profession']}\n\n...")
    higher_followercount = a if float(a['followers']) >= float(b['followers']) else b
    is_correct = check_answer(a, b, user)
    while (is_correct) :

        a = higher_followercount
        b = random.choice(data_list)
        higher_followercount = a if float(a['followers']) >= float(b['followers']) else b

        user = input(f"\n\nWho has more followers?...\n\n {a['name']}, {a['profession']}\n\tOR\n {b['name']}, {b['profession']}\n\n...")
        is_correct = check_answer(a, b, user)

    #print(a['name'] + ' ' + a['followers'])
    #print(b['name'] + ' ' + b['followers'])
    #print(higher_follower)

    active = False
