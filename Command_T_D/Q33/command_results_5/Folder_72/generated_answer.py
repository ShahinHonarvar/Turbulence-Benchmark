import re
def return_vowels(s):
    return re.findall(r'[aeiou]{%d,%d}' % (37, 57))
