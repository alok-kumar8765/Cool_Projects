import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y" or 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
# print(translate(word))
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

# ==== ROUGH WORK START ====

"""
import difflib
from difflib import SequenceMatcher
SequenceMatcher(None, "rainn", "rain").ratio()
"""

"""
from difflib import get_close_matches
help(get_close_matches)
get_close_matches("rainn", ["help", "pyramid", "rain"])
get_close_matches("rainn", data.keys())
get_close_matches("rainn", data.keys())[0]
"""
# ==== ROUGH WORK END ====