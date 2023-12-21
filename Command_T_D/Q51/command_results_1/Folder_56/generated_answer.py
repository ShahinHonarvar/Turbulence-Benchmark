import re
def if_contains_anagrams(s):
    return bool(re.findall(r"([A-Z]+[a-z]+)+", s, flags=re.I))
