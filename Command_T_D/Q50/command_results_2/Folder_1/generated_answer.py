import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z]))([a-z]+)\1', ' '.join(s), flags=re.I))
