import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?:(?P<s>[A-Z])\1)+\1\1+)+', s))
