print("rock,paper,scissors...")
print("Please don't use upper case or camel case. Use the same text as above!")
Player_1 = input("Player 1,please put in your name. ")
Player_2 = input("Player 2,please put in your name. ")
Player_1_answer = input(f"{Player_1} 1,rock,paper,or scissors? ")
print("!!!!$$$$DON'T CHEAT$$$$!!!!\n" * 65)

Player_2_answer = input(f"{Player_2},rock,paper,or scissors? ")
print("SHOOT!!!")
if Player_1_answer == "rock":
    if Player_2_answer == "scissors":
        print(f"{Player_1} wins!")
    elif Player_2_answer == "paper":
        print(f"{Player_2} wins!")
    else:
        print("It is a tie!! Try again!")
# next
elif Player_1_answer == "paper":
    if Player_2_answer == "scissors":
        print(f"{Player_2} wins!")
    elif Player_2_answer == "rock":
        print(f"{Player_1} wins!")
    else:
        print("It is a tie!! Try again!")
# final
elif Player_1_answer == "scissors":
    if Player_2_answer == "paper":
        print(f"{Player_1} wins!")
    elif Player_2_answer == "rock":
        print(f"{Player_2} wins!")
    else:
        print("It is a tie!! Try again!")
else:
    print("Make sure you check the spelling and remember, Python is case sensitive.")