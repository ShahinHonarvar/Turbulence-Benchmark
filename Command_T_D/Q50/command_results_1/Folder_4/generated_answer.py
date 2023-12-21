import re
def if_contains_anagrams(s):
    return bool(re.findall(r'\A[a-z]{3}[\d]{4}([a-z]){3}\1', s))
