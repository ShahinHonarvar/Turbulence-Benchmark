import re
def if_contains_anagrams(s):
    res = re.findall(r"((?:[a-z]){3})\1", "".join(s).lower())
    return len(res) >= 312
