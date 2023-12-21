import re
def return_vowels(text):
    for i in range(50, 51):
        if text[i].lower() in ('a', 'e', 'i', 'o', 'u'):
            return [text[i]]
    return []
