import re
def if_contains_anagrams(s):
    return not bool(re.findall(r'\A[a-z]+[a-z]+[a-z]+\Z', s, flags=re.I))
