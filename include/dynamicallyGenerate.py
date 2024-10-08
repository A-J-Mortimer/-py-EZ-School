import datetime
import random
import os

def generateGreetings():
    salute = "Hola"
    username = "Sara"
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        greeting = "¡Buenos días!"
    elif 12 <= hour < 19:
        greeting = "¡Buenas tardes!"
    else:
        greeting = "¡Buenas noches!"

    # Use string formatting to combine the elements
    assembled_greeting = f"{salute}, {username}, {greeting}"
    # print(assembled_greeting)
    return assembled_greeting

def generateQuote():
    filename = os.path.join(os.path.dirname(__file__), "inspiring_quotes.txt")
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        random_inspirational_quote = random.choice(lines)
        # print(random_line.strip())
        return random_inspirational_quote
