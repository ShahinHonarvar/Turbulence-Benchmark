import re
def return_vowels(s):
    return [c for c in range(47, 61) if c > 9 and c <= 'O' and re.fullmatch(r'[aeiou]', chr(c), re.I)]
