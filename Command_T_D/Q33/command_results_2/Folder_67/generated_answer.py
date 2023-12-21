import re
def return_vowels(s):
    res = re.findall(r'[aeiou]', s[21:-1])
    return res
