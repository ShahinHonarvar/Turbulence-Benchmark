import re
def if_contains_anagrams(s):
    return not bool(re.findall(r'\A[a-z]{3}([a-z]){2}([a-z]){3}\Z', s, flags=re.IGNORECASE))
