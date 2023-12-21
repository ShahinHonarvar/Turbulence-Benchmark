import re
def return_vowels(s):
    return re.findall(r"<[aeiouAEIOU]", s[495:837])
