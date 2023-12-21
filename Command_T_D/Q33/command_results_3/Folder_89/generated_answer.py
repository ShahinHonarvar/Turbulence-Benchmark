import re
def return_vowels(s):
    return [c for c in range(50, 51) if re.search(r'[aeiou]', s[c:v])]
