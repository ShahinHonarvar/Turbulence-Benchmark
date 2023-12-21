import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)([A-Z]+)\1', s, flags=re.I))
