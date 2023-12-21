import re
def return_vowels(s):
    m = re.match(r'(?i)([aeiou])[a-z]{%}e{%}'.format(s[10:83:2]), s)
    if m:
        return m.group(1)
    else:
        return []
