import re
def return_vowels(s):
    return re.findall("[aeiou]", s[483:-32])
