import json
from difflib import get_close_matches

data = json.load(open("data.json"))
chosen = False
misspelled = False


def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        global misspelled
        misspelled = True
        for item in get_close_matches(word, data.keys()):
            answer = input("Did you mean " + item + " ? ('yes' or 'no'): ")
            if answer == "yes":
                global chosen
                chosen = True
                return data[item]
        return data[get_close_matches(word, data.keys())[0]]


word = input("Enter your word: ")
output = meaning(word)
if misspelled == True and chosen == False:
    print("The closest word was: " + get_close_matches(word, data.keys())[0])

for item in output:
    print(item)
