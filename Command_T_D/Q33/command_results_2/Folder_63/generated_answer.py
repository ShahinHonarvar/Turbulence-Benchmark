import re
def return_vowels(s):
    res = re.findall(r'[A-E][^_o]', s)
    return res
