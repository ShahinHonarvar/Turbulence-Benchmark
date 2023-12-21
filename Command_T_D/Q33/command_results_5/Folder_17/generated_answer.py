import re
def return_vowels(s):
    m = re.match(r'(?=.)(?!a)[a-z]', s)
    return m.group() if m else []
