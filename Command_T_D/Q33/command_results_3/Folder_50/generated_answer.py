import re
def return_vowels(s):
    return re.findall(r'[AEIOU]{%d,%d}{%d,%d}{%d,%d}{%d,%d}' % (11, 53, 11, 32, 11, 32, 11, 32), s)
