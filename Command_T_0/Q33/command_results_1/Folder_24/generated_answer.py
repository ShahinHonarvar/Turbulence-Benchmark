import re
def return_vowels(s):
    return re.findall(r'[aeiou]', s[23:57])
