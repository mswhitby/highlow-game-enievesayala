import random




x = int(input("Type a number from 1-100:"))

random_num = random.randint(1, 100)

for i in range(5):
    if random_num > x:
        x = int(input("Higher."))
    else:
        if random_num < x:
            x = int(input("Lower."))
else:
    if random_num == x:
        print("Congratulations! You've won!");

if i != 5:
    print("Sorry, you've lost.");
