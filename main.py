import random


random_integer = random.randint(1,10)
print(random_integer)

inputNum = int(input("Enter a value between 1 and 10 "))

x = range(1,11)

if inputNum in x  and inputNum == random_integer:
    print(inputNum)
else:
    print("invalid Input")




