import re
def return_vowels(s):
    return re.findall(r"(([aeiou])\w+)", s)[1:-1]
