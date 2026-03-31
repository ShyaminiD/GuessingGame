import random


random_integer = random.randint(1, 10)
print(random_integer)

user_input = input("Enter a value between 1 and 10 ").strip(' *"')
try:
    inputNum = int(user_input)
    x = range(1, 11)
   

    if inputNum not in range(1, 11):
        print(" Entered Number is out of Range", list(x))

    elif inputNum == random_integer:
        print("CORRECT GUESS!!!", inputNum, random_integer)
    else:
        print("OOPS, INCORRECT GUESS")
except:
    print("Enter a valid number")
