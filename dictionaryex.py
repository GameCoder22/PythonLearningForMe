num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


p = len(num) - 1

print("COUNTDOWN")

while p >= 0:
    print(num[p])
    p -= 1
    if p == 0:
        print(num[p])
        print("BLASTOFF!!!")
        break
