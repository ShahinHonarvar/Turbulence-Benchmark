import re
def return_vowels(s):
    return re.findall(r'[A-x]+[aeiou]', s)
