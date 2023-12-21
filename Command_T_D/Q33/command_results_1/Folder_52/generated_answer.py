import re
def return_vowels(s):
    return [c for c in range(ord("g"), ord("z") + 1) if c in s and c not in re.findall(r"f||", s)]
