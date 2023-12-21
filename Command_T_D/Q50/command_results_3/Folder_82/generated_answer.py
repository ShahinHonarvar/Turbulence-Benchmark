import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z][^A-Z]*[A-Z]))([A-Z][^A-Z]*[A-Z])', s, flags=re.I))
