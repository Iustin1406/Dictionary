import json
from difflib import get_close_matches
data = json.load(open("data.json"))
other_possibilities=False
def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("The closest word is: " + get_close_matches(word,data.keys())[0])
        global other_possibilities
        other_possibilities=True
        return data[get_close_matches(word,data.keys())[0]]


word = input("Enter your word: ")
output = meaning(word)
for item in output:
    print(item)
if other_possibilities==True:
    print("All possible words were:")
    print(*get_close_matches(word,data.keys()),sep=', ')