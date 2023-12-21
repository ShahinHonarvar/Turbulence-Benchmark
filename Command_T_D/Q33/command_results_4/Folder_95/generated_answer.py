import re
def return_vowels(s):
    res = re.findall(r'[A-Z][^?P]+', s)
    return res
