import re
def return_vowels(s):
    return re.findall(r'[aeiou]b', s)[10:-1]
