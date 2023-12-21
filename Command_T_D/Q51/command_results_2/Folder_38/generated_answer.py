import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?:[a-z])\1+', '|'.join(s), flags=re.I))
