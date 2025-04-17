# Day 4 project
import rock, paper, scissors, random

choices = [rock.rock, paper.paper, scissors.scissors]
user = int(input("Rock (1), Paper (2), or Scissors (3)?\n"))
user_choice = choices[user-1]
computer = random.randint(1, 3)
computer_choice = choices[computer-1]

print(f"{user_choice}")
print(f"Computer chose: \n{computer_choice}")

# rock scissors = rock wins
# rock paper = paper wins
# paper scissors = scissors wins

if user == computer:
    print("Draw!")
elif user == 1 and computer == 2:
    print("Computer Wins!")
elif user == 2 and computer == 1:
    print("User wins!")
elif user == 1 and computer == 3:
    print("User wins!")
elif user == 3 and computer == 1:
    print('Computer wins!')
elif user == 2 and computer == 3:
    print('Computer wins!')
elif user == 3 and computer == 2:
    print('User wins!')



