import math

# theory: for every n, there are two numbers a, b, such that a x b = n
# best case, a, b = sqrt(n)
# so we would only have to check numbers 2 through sqrt(n) (sqrt(n) + 1 in python since python floors the sqrt)
# anything less than 2 would automatically not be a prime number

def is_prime(number):
    if number <= 1:
        return False
    else:
        prime = True # assume true, then try to disprove
        for i in range(2, math.sqrt(number)+1):
            if number%i==0:
                prime = False
                break # immediately break if false

    return prime