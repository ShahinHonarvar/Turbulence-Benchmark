import re
def return_vowels(s):
    res = re.findall(r'[A-E][^b]*[A-O]', s)
    return res
