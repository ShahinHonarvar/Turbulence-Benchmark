import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z][a-z]{2,})[A-Z][a-z]{2,})', s, flags=re.I))
