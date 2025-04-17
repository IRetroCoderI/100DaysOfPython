import random
import art 
# cards in a deck: A 1 2 3 4 5 6 7 8 9 10 J Q K 
# J Q K = 10 each
# A = 1 or 11
cards = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# cases where game ends:
    # player goes over 21 -> finish computers hand, most likely winner
    # player decides no more cards -> finish computers hand, decide winner

# special things to consider:
    # player receives an ace, decide if 1 or 11

def check_for_ace(player_hand):
    if 'A' in player_hand:
        response = input("Ace in player hand, type '1' or '11' to apply points: ")
        if response == '1':
            player_hand[player_hand.index('A')] = 1
        elif response == '11':
            player_hand[player_hand.index('A')] = 11
    
    return player_hand

def computer_check_for_ace(computer_hand):
    # auto choose the best value for Ace
    while 'A' in computer_hand:
        # If treating Ace as 11 wouldn't bust, use 11, otherwise use 1
        current_sum = sum([card for card in computer_hand if card != 'A'])
        if current_sum + 11 <= 21:
            computer_hand[computer_hand.index('A')] = 11
        else:
            computer_hand[computer_hand.index('A')] = 1
    
    return computer_hand

def check_for_blackjack(player_hand, computer_hand):
    if sum(computer_hand) == 21 and sum(player_hand) != 21:
        print("COMPUTER HAS BLACKJACK, YOU LOSE")
    elif sum(computer_hand) == 21 and sum(player_hand) == 21:
        print("BOTH COMPUTER AND PLAYER HAVE BLACKJACK, PUSH, BETS RETURNED")
    elif sum(computer_hand) != 21 and sum(player_hand) == 21:
        print("BLACKJACK! PLAYERWINS")

def end_game(player_hand, computer_hand):
    print()
    if sum(player_hand) == sum(computer_hand):
        print("\tDRAW! YOU ARE ALL WINNERS")
    elif sum(player_hand) > sum(computer_hand):
        print("\tCONGRATULATIONS, YOU WIN!")  
    elif sum(player_hand) < sum(computer_hand):
        print("\tCOMPUTER WINS, YOU LOSE!")

def play_game():
    print(art.black_jack_art)
    player_hand = [random.choice(cards), random.choice(cards)]
    computer_first_card = random.choice(cards)
    computer_hand = [computer_first_card, random.choice(cards)]
    check_for_ace(player_hand)
    check_for_ace(player_hand)

    computer_hand = computer_check_for_ace(computer_hand)

    if sum(player_hand) == 21 or sum(computer_hand) == 21:
        check_for_blackjack(player_hand, computer_hand)
        user = 'n'

    print(f"\tYour cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"\tComputer's first card: {computer_first_card}")
    

    # ask user to draw another card, if y, send to function
    user = ''
    while user != 'n':
        user = input("Type 'y' to get another card, type 'n' to pass: ")
        if user == 'y':
            drawn_card = random.choice(cards)
            check_for_ace([drawn_card])
            player_hand.append(drawn_card)
            
            print(f"\tYour cards: {player_hand}, current score: {sum(player_hand)}")
            print(f"\tComputer's first card: {computer_first_card}")

            if sum(player_hand) == 21 or sum(computer_hand) == 21:
                check_for_blackjack(player_hand, computer_hand)
                return

            elif sum(player_hand) > 21:
                print(f"\tYour final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"\tComputer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("Player has went over 21, you lose.")
                return


    # if user 'n', give score then return to game loop
    print(f"\tFinal result hand: {player_hand}, score: {sum(player_hand)}")
    while sum(computer_hand) < 16:
        if sum(computer_hand) > 21:
            print("Computer over 21, player wins")
        else: 
            computer_hand.append(random.choice(cards))
            computer_hand = computer_check_for_ace(computer_hand)
    print(f"\tFinal computer result: {computer_hand}, score: {sum(computer_hand)}")

    end_game(player_hand, computer_hand) # decides winner
    return

    # after player receives initial hand of two cards and checked for aces, will be asked if they want another card
        # no -> end game, count score and find winner
        # yes -> draw new card, check for ace, computer draws card

active = True
while active:
    user = input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user == 'n': # user does not want to play a game of blackjack
        active = False
    elif user == 'y': # user wants to play blackjack
        play_game()
        
        
        

