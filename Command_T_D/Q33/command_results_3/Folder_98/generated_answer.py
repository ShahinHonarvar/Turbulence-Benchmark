import re
def return_vowels(s):
    m = re.match(r'[a-z]{%d,{%d}}[a-z]{%d,{%d}}' % (3, 6, 3, 6), s)
    if m:
        return m.group(1, 2)
    else:
        return []
