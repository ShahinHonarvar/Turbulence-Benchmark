import re
def return_vowels(s):
    s = re.sub(r'[^A-Z]', '', s)
    return [c for c in s if c.isalpha() and c.lower() in 'AEIOU']
