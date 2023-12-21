import re
def return_vowels(str1):
    res = re.findall(r'([aeiou])\W', str1)
    return res
