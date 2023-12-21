import re
def return_vowels(s):
    return [c for c in s[22:82] if re.match(r'[aeiou]', c)]
