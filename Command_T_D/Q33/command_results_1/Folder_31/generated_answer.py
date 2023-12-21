import re
def return_vowels(s):
    r = re.findall(r'[aeiou]', s)
    return [c for c in r if c.isupper() and c.isalpha() and c.isalnum()]
