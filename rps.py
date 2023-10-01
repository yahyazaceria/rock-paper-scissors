import random
import sys

user = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user > 2:
    print("I could not understand. You lost!")
    sys.exit()

computer = random.randint(0, 2)

if user == 0:
    print("You Chose: Rock")
elif user == 1:
    print("You Chose: Paper")
elif user == 2:
    print("You Chose: Scissors")

if computer == 0:
    print("Computer Chose: Rock")
elif computer == 1:
    print("Computer Chose: Paper")
elif computer == 2:
    print("Computer Chose: Scissors")

if computer == 0 and user == 2:
    print("You lost!")
elif computer == 2 and user == 0:
    print("You won!")
elif computer > user:
    print("You lost!")
elif user > computer:
    print("You won!")
elif computer == user:
    print("Draw!")

