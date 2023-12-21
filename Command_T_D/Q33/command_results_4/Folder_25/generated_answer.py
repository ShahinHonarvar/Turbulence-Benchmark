import re
def return_vowels(s):
    return re.findall(r'[aeiou][A-Z]{%d,%d}'.format(s.index('+') + 1, s.index('z') - 1), s)
