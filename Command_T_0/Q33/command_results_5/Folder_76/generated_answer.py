import re
def return_vowels(s):
    return re.findall(r'[A-Z][^B-t]', s[495:837])
