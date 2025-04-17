#Day 2 project
#this program takes the total from the user, the amount they want to tip, and how many people are splitting the bill

total = float(input("\tWhat is the bill's total?: $"))
tip = int(input("\tWhat would you like to tip? 10, 15, 20?: "))
numPeople = int(input("\tHow many people are splitting the bill?: "))

totalWithTip = (total*(tip/100)) + total
split = totalWithTip/numPeople
res = 5
print(f"\tEvery person pays: ${str(round(split, 2))}")

