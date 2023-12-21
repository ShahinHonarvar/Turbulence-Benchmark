import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(\d\d)(?:\d)(\d)', ' '.join(s), flags=re.I))
