import requests
import random
from pyfiglet import Figlet

url = "https://icanhazdadjoke.com/search"

def service_check():
    response = requests.get(url)
    is_ready = "online" if response.ok else "offline"
    return is_ready

def search_joke(topic):
    try:
        response = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": topic} 
            #https://icanhazdadjoke.com/search?term=cat&limit=1
        )

        data = response.json()
        pick_random_joke = random.randrange(len(data["results"]))
        return data["results"][pick_random_joke].get('joke')

    except ValueError:
        return "Sorry, I don't have results for " + topic + " | Try again!"

def show_joke(joke):
    sep="="
    for num in range(len(joke)):
        sep += "="
    print(sep)
    print(joke)
    print(sep)

    
f = Figlet(font='slant')
print( f.renderText("Joke MACHINE"))
print("status: " + service_check())
topic = input("Let me tell you a joke! Give me a topic: ")

joke = search_joke(topic)

show_joke(joke)


