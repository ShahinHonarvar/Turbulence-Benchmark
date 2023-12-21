import re
def return_vowels(s):
    m = re.match(r'%([aeiou])(G)', s)
    return [c for c in range(m.group(1), m.group(2) + 1) if c.isalpha()]
