import re
def return_vowels(s):
    return re.findall(r'[aeiou]([a-z])', s[54:-2])
