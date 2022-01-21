print("Welcome to my homemade calulator!!")
final = input("Do you have a question?")
# arithmatical
def num_add(num1,num2):
    int(num1,num2)
    return num1 + num2

def num_sub(num1,num2):
    int(num1, num2)
    return num1 - num2

def num_multi(num1,num2):
    int(num1, num2)
    return num1 * num2

def num_divide(num1,num2):
    int(num1, num2)
    return num1 / num2

# sqares and cubes
def num_sqare(num):
    int(num)
    return num * num

def num_cube(num):
    int(num)
    return num * num * num

# additional





# calculaotor
if final == "yes":
    math = input("What do u want to do? ")
    if math == "add":
       x = input("What is your number 1? ")
       int(x)
       y = input("What is your number 2? ")
       int(y)
       print(num_add(x,y))
    elif math == "substract" or "sub":
       x = input("What is your number 1? ")
       int(x)
       y = input("What is your number 2? ")
       int(y)
       print(num_sub(x,y))
    elif math == "multi" or "multiply":
       x = input("What is your number 1? ")
       int(x)
       y = input("What is your number 2? ")
       int(y)
       print(num_multi(x,y))
    elif math == "divide" or "div":
       x = input("What is your number 1? ")
       int(x)
       y = input("What is your number 2? ")
       int(y)
       print(num_divide(x,y))
    elif math == "square":
        z = input("What is your number you want to square? ")
        print(num_sqare(z))
    elif math == "cube":
        z = input("What is your number you want to cube? ")
        print(num_cube(z))
    else:
        print("INVALID")
else:
    print("Bye👋")
