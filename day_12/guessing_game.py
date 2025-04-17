import random

active = True
while active:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    #print(f"Pssst, the correct answer is {number}")
    user = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user == 'easy':
        attempts = 10
    elif user == 'hard':
        attempts = 5
    elif user == 'q':
        active = False
        continue

    won_game = False
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess > number:
            print("Too high.")
            print("Guess again.")
        elif guess < number:
            print("Too low")
            print("Guess again")
        else:
            print("Correct!")
            won_game = True
            break

    if not won_game:
        print(f"You ran out of attempts, the correct answer was {number}\n\n")
    

        