import re
def return_vowels(s):
    m = re.search(r'[aeiou][a-z][a-z0-9][a-z]', s)
    return [c for c in range(20, 43) if c in m.group()]
