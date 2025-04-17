import os


bidders = {
    
} # empty dictionary, will contain user_name, and their bid, like so
# jesus: 25
# angie: 12
print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
''')
active = True
while(active):
    print('\nWelcome to the secret auction program.')
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: $"))
    bidders[user_name] = user_bid
    response = input("Are there any other bidders? Type 'yes' or 'no' ")
    if response == 'yes': 
        active = True
        os.system('clear')
    elif response == 'no': active = False


#print(bidders) for debugging

def find_winner(bidders):
    highest_bid = 0
    highest_bidder = ''
    for key in bidders:
        highest_bid = max(highest_bid, bidders[key])
    for key in bidders:
        if bidders[key] == highest_bid:
            highest_bidder = key
    print("*****************************************************************")
    print(f"Winner of Auction: {highest_bidder}\nWinning bid: ${highest_bid}")


find_winner(bidders)