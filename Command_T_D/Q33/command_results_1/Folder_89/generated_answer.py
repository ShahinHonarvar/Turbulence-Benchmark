import re
def return_vowels(s):
    return [m for m in re.finditer(r'[aeiou]', s[50:-1]) if m.start() >= 50 and m.end() <= 51]
