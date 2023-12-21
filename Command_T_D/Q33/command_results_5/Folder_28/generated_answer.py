import re
def return_vowels(s):
    return [c for c in range(ord("A"), ord("Z") + 1) if c in re.findall(r"<[AEIOU]>", s)]
