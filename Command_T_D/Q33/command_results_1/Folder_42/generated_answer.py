import re
def return_vowels(s):
    m = re.search(r'[aeiou]{%d,%d}[^|;]+' % (12, 39), s)
    return m.group()
