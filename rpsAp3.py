import random

wins = 0
aiwins = 0
rec = 3
print("rock,paper,scissors...")
Player_1 = input("What is your username? ")


while wins < rec and aiwins < rec:
    numdom = random.randint(1, 3)

    if numdom == 1:
        aians = "Rock"
    elif numdom == 2:
        aians = "Paper"
    else:
        aians = "Scissors"

    print(f"{Player_1}'s score: {wins}, Computer's score: {aiwins}")
    Player_1_answer = input(f"{Player_1} ,rock,paper,or scissors? ")

    print("SHOOT!!!")
    if Player_1_answer == "rock" or "1":
        if aians == "Scissors":
            print(f"{Player_1} wins!")
            aiwins += 1
        elif aians == "Paper":
            print(f"The computer wins!")
            wins += 1
        else:
            print("It is a tie!! Try again!")
    # next
    elif Player_1_answer == "paper" or "2":
        if aians == "Scissors":
            print(f"The computer wins!")
            aiwins += 1
        elif aians == "Rock":
            print(f"{Player_1} wins!")
            wins += 1
        else:
            print("It is a tie!! Try again!")
    # final
    elif Player_1_answer == "scissors" or "3":
        if aians == "Paper":
            print(f"{Player_1} wins!")
            wins += 1
        elif aians == "Rock":
            print(f"The computer wins!")
            aiwins += 1
        else:
            print("It is a tie!! Try again!")
    elif aiwins or wins == rec:
        if aiwins == rec:
            final = "Computer wins!"
            print(final)
        if wins == 3:
            final = "You win!"
            print(final)
    elif Player_1_answer == "quit":
        print("Bye.")
        print(f"FINAL SCORE: {Player_1}'s score: {wins}, Computer's score: {aiwins}")
        break
    else:
        print("Make sure you check the spelling and remember, Python is case sensitive.")

    print(f"In case you wanted to know, the computer played: {aians}")

print(f"FINAL SCORE: {Player_1}'s score: {wins}, Computer's score: {aiwins}")