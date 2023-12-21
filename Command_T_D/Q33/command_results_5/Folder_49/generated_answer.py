import re
def return_vowels(s):
    return re.findall(r'[aeiou]{10,}(?<=b)', s)
