import re
def return_vowels(s):
    res = re.findall("[aeiou]", s[28:76])
    return res
