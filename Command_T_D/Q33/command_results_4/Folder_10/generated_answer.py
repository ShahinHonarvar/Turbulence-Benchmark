import re
def return_vowels(s):
    res = re.findall(r'[aeiou]', s[31:-2])
    return res
