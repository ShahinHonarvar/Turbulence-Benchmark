import re
def return_vowels(str1):
    res = re.findall(r'[aeiou]', str1[20:41])
    return res
