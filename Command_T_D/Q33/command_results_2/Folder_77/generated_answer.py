import re
def return_vowels(s):
    return [c for c in range(837, 975) if c in s and c in re.findall(r'[aeiou]', s)]
