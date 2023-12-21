import re
def if_contains_anagrams(s):
    return bool(re.findall(r'\A[A-Z]{3}([A-Z][a-z]){2}\Z', s, flags=re.I))
