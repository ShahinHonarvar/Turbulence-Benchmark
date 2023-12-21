import re
def return_vowels(s):
    i, j = 2, 7
    return re.findall(r'[aeiou]', s[i:j])
