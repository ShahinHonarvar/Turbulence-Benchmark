import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=.*[aeiou])(?=.*[aeiou])(?=.*[a-z])(?=.*[a-z])\1\2\3', s))
