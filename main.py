import random




x = int(input("Type a number from 1-100:"))

random_num = random.randint(1, 100)

while x != random_num:
    if random_num > x:
        x = int(input("Higher."))
    else:
        if random_num < x:
            x = int(input("Lower."))
else:
    if random_num == x:
        print("Congratulations! You've won!");
