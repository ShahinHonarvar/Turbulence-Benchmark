import re
def return_vowels(s):
    res = re.findall(r'[aeiou](?=[dD])[a-v]', s)
    return res
