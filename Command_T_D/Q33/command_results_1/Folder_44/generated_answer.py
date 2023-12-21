import re
def return_vowels(str1):
    res = re.findall(r'[aeiou]', str1[46:49])
    return res
