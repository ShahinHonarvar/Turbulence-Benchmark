import re
def return_vowels(str):
    res = re.findall(r'[A-Z][^A-Z]*[A-Z]', str)
    return res
