import random

someNums = [10, 15, 2, 3, 4, 5, 6, 8, 22, 10, 'a', 'b', 't', 'i', 'x']
my_ticket = [15]

randomNum = random.choice(someNums)
i = 0

while(True):
    i += 1
    print(randomNum)
    if randomNum == 15:
        print(f"Your ticket is a winner!, The loop ran {i} times...")
        break
    randomNum = random.choice(someNums)