import re
def if_contains_anagrams(s):
    return bool(re.findall(r"((?i)(?:(?P<x>.*[A-Z])\1)+)", s))
