import random

while True:
    print("Make a guess between 1 to 100")
    player = int(input('Make a guess! '))
    int(player)
    randnum = random.randint(1, 100)
    # noinspection PyStatementEffect
    int
    if player < randnum:
        print("It is lower than the random number. ")
    if player > randnum:
        print("It is higher than the random number. ")

    else:
        print("YOU WON!!!!")
        again = input("Do you want to play?(y/n) ")
        if again == "y":
            randnum = random.randint(1, 100)
            player = None
        else:
            print("BYE")
            break
