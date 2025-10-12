"""
  1 => Snake
  0 => Gun
 -1 => Water 

"""

import random

computerChoice = random.choice([-1, 0, 1])
userChoice = input("What is your choice (S : Snake || w : Water || g: Gun) ::  ")

userToNum = {"s" : 1, 
             "w" : -1,
             "g" : 0}

getUserInput = userToNum[userChoice]
print(getUserInput)
print(computerChoice)
numToStr = {1:"Snake", 0:"Gun" , -1:"Water"}
userOutput = numToStr[getUserInput]
computerOutput = numToStr[computerChoice]

if(getUserInput == computerChoice):
    print("Match Draw !!!")
else:
    if(computerChoice == 1 and getUserInput == 0):
        print("You Win!🥳")
    elif(computerChoice == 1 and getUserInput == -1):
        print("You Loss! 😔")

    elif(computerChoice == 0 and getUserInput == -1):
        print("You Win!🥳")
    elif(computerChoice == 0 and getUserInput == 1 ):
        print("You Loss! 😔")


    elif(computerChoice == -1 and getUserInput == 1):
        print("You Win!🥳")
    elif(computerChoice == -1 and getUserInput == 0 ):
        print("You Loss! 😔")
