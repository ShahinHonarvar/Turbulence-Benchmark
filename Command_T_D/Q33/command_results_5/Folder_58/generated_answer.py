import re
def return_vowels(s):
    m = re.fullmatch(r'<[a-z]*>', s)
    if m:
        return m.group()
    else:
        return ['']
