import requests
import pyfiglet
import random
import termcolor
header = pyfiglet.figlet_format("DAD!")
nice = termcolor.colored(header, color="blue")
print(nice)
user_input = input("What dad jokes kind of do you want? ")
url2 = "https://www.youtube.com/watch?v=gnV-8pkILF0"
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num_res = res["total_jokes"]
results = res["results"]
if num_res > 1:
    print(f"There are {num_res} jokes about {user_input}. Here is one:")
    print(random.choice(results)["joke"])
elif num_res == 1:
    print(f"There is one joke about {user_input}.")
    print(results[0]['joke'])
else:
    print(f"Sorry. There is no joke about {user_input}.")



