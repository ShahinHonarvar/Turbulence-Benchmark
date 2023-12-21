import re
def return_vowels(s):
    return re.findall("[aeiouAEIOU]", s[1:-1])
