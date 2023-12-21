import re
def return_vowels(str1):
    res = re.findall(r'[aeiou]', str1[5:])
    return res
