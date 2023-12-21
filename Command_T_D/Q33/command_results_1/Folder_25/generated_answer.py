import re
def return_vowels(s):
    m = re.findall(r'[aeiou]([A-Z]{%d,%d})[A-Z]{%d,%d}' % (29, 75, 29, 75), s)
    return m
