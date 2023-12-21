import re
def return_vowels(str):
    m = re.match(r'[aeyuio]+', str)
    return m.group() if m else []
