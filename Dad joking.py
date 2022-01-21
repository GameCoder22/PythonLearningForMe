import requests
topic = input("What dad jokes kind of do you want? ")
url2 = "https://www.youtube.com/watch?v=gnV-8pkILF0"
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic, }
)