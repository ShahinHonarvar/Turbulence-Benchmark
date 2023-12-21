import re
def return_vowels(s):
    return re.findall(r'[A-U]+', s, flags=re.I)
