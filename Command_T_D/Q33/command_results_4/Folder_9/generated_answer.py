import re
def return_vowels(s):
    return re.findall(r'[aeiou]([a-f])', s)[1:-1]
