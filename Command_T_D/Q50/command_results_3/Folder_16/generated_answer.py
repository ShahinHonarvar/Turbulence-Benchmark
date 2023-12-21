import re
def if_contains_anagrams(s):
    return bool(re.findall(r'\A[a-z]{3}]+\Z', ''.join(s), flags=re.I))
