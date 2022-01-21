import random


numdom = random.randint(1,3)

if numdom == 1:
    aians = "Rock"
elif numdom == 2:
    aians = "Paper"
else:
    aians = "Scissors"

print("rock,paper,scissors...")
print("Please don't use upper case or camel case. Use the same text as above!")
Player_1 = input("What is your username? ")
Player_1_answer = input(f"{Player_1} ,rock,paper,or scissors? ")

print("SHOOT!!!")
if Player_1_answer == "rock":
    if aians == "Scissors":
        print(f"{Player_1} wins!")
    elif aians == "Paper":
        print(f"The computer wins!")
    else:
        print("It is a tie!! Try again!")
# next
elif Player_1_answer == "paper":
    if aians == "scissors":
        print(f"The computer wins!")
    elif aians == "Rock":
        print(f"{Player_1} wins!")
    else:
        print("It is a tie!! Try again!")
# final
elif Player_1_answer == "scissors":
    if aians == "Paper":
        print(f"{Player_1} wins!")
    elif aians == "Rock":
        print(f"The computer wins!")
    else:
        print("It is a tie!! Try again!")
else:
    print("Make sure you check the spelling and remember, Python is case sensitive.")

print(f"In case you wanted to know, the computer played: {aians}")