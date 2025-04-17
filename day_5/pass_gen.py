# Day 5 project
import random
import string
import pyperclip


password_chars = [] #empty list
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', 
                        '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", 
                        '<', '>', ',', '.', '?', '~']

letters = string.ascii_lowercase + string.ascii_uppercase

num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like?\n'))
num_numbers = int(input('How many numbers would you like?\n'))


for a in range(0, num_numbers): 
    password_chars.append(random.randint(0, 9))
for b in range(0, num_letters):
    password_chars.append(random.choice(letters))
for c in range(0, num_symbols):
    password_chars.append(random.choice(special_chars))

random.shuffle(password_chars)
password = ''
for i in password_chars:
    password += str(i)


pyperclip.copy(password)
print(f"\n{password}")
print("Password has been copied to clipboard.")




