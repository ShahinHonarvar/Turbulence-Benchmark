import re
def return_vowels(s):
    m = re.findall(r'[aeiou]{,5}', s[202:-1])
    return m
