import re
def return_vowels(s):
    m = re.search(r'[A-Z][^@]{%d,%d}' % (10, 82), s)
    return m.group()
