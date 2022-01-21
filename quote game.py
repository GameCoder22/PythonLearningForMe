import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    # print(f"Now scraping {base_url}{url}")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")


    for quote in quotes:
        all_quotes.append({
            "text" : quote.find(class_="text").get_text(),
            "author" : quote.find(class_="author").get_text(),
            "bio-link" : quote.find("a") ["href"]
            })


    next_btn = soup.find(class_="next")
    url = next_btn.find("a") ["href"] if next_btn else None
    sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000001)




def start_game():
    quote = choice(all_quotes)
    rem_guesses = 4
    print("Here is a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    guess = input(f"Who said this quote? Guesses remaining {rem_guesses}: ")
    if guess.lower() == quote["author"].lower():
        print("YOU WIN")
        print("You got it right!")
    rem_guesses -= 1
    if rem_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here is a hint: the author was born on {birth_date} {birth_place}.")

    elif rem_guesses == 2:
        print(f"Here's a hint: The author's first name starts with: {quote['author'] [0]}")

    elif rem_guesses == 1:
        last_initial = quote["author"].split(" ")[1] [0]
        print(f"Here's a hint: The author's last name starts with: {last_initial}")

    else:
        print("GAME OVER")
        print(f"You ran out of guesses. The answer was {quote['author']}")


    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n): ")
    if again.lower() in ('y', 'yes'):
        print("Okay, you can play again.")
        return start_game()
    else:
        print("Bye!")

start_game()

