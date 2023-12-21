import re
def return_vowels(s):
    return re.findall(r"([aeiou])\B", s[40:-1])
