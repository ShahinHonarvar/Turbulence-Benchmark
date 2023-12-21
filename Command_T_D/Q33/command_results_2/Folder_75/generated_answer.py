import re
def return_vowels(s):
    m = re.match(r'[A-Z][^K-Z]*', s)
    if m:
        return m.group()
    else:
        return []
