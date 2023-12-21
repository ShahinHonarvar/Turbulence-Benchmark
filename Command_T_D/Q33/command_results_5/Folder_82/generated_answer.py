import re
def return_vowels(s):
    return re.findall(r'[AEIOU]{86,99}r', s)
