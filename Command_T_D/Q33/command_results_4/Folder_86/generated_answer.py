import re
def return_vowels(s):
    return re.findall(r'[aeyuio]', s[273:-1])
