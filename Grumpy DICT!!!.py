class GrumpyDict(dict):
    def __repr__(self):
        print("HEEEEEEEEEEY!!!WHY YOU MESSING AROUD WITH ME? FINE HAVE IT!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU GOT IT WRONG!!!! ({key}) ISN'T HERE!!")

    def __setitem__(self, key, value):
        print("HOW DARE YOU TRY TO CHANGE THE DICT!!!!!!")
        print("IF YOU HAVE MONEY, THEN... SURE,OKAY.")
        super().__setitem__(key, value)

data = GrumpyDict({"hi" : "bonjour", "bye" : "au revoir"})
print(data)
data["spanish_hi"] = "hola"
print(data)
