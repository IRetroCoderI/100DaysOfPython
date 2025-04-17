import operator

print(r'''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv    
}

def calculate(a, b, operation):
    if operation in ops:
        return ops[operation](a, b)
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    
def continue_operation(number):
    operation = input("Pick an operation: ")
    second_num = float(input("What's the next number?: "))
    result = calculate(number, second_num, operation)
    print(f"{number} {operation} {second_num} = {result}")
    user = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if user == 'n':
        return
    elif user == 'y':
        continue_operation(result)


active = True
while(active):
    first_num = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    second_num = float(input("What's the next number?: "))
    result = calculate(first_num, second_num, operation)
    print(f"{first_num} {operation} {second_num} = {result}")
    user = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if user == 'n':
        continue
    elif user == 'y':
        continue_operation(result)

    