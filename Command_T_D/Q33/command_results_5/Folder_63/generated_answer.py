import re
def return_vowels(string):
    return [c for c in string[34:-1] if c.isalpha() and c.lower() in 'aeiou']
