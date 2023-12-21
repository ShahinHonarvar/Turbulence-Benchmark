import re
def return_vowels(s):
    return re.findall(r'[aeiou]([A-Z]?)', s)[1:]
