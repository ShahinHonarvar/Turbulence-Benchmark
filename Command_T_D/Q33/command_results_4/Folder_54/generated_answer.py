import re
def return_vowels(s):
    return re.findall(r'([^W][aeiou])', s)
