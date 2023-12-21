import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?:[A-Z][a-z]{2,}){12}', ' '.join(s), flags=re.I))
