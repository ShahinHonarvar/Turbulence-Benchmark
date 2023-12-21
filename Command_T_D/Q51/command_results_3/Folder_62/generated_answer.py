import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)([A-Z][^A-Z]*[A-Z])\1', ' '.join(s), flags=re.I))
