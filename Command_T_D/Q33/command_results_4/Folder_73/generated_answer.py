import re
def return_vowels(s):
    res = re.findall(r'[aeiou]{47,89}', s)[1:]
    return res
