import re
def if_contains_anagrams(s):
    return bool(re.findall(r"(?=([a-z]+){3}[A-Z][a-z]?)\1", "".join(s), re.I))
