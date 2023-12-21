import re
def return_vowels(s):
    m = re.match(r'[A-Z]{3,}(?<=\b[A-Z];)t', s)
    return m.group()
