import re
def if_contains_anagrams(s):
    return bool(re.findall(r'\A[a-z]+\d+[a-z]+', s, flags=re.I))
