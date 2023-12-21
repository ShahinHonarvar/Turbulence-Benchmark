import re
def return_vowels(s):
    return re.findall(r'[AEIOU]', s[1:7])
