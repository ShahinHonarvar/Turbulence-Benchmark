import re
def return_vowels(str1):
    res = re.findall(r'[aeiou]', str1[82:-1])
    return res
