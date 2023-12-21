import re
def if_contains_anagrams(s):
    return bool(re.findall(r"(\A[A-Z]+[a-z]+[A-Z]+)+", "".join(s), flags=re.I))
