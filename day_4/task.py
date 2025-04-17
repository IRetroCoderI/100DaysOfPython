# day 4
import random
import my_module

num = random.randint(1, 100)
count = 1
while (num != 1):
    print(num)
    num = random.randint(1, 100)
    count = count + 1
print(num)
print(f"That took {count} tries")