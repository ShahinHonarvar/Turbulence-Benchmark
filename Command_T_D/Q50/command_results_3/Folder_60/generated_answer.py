import re
def if_contains_anagrams(lst):
    return bool(re.findall(r"((?i)[a-z]){3}((?i)[a-z]){3}", "".join(lst), flags=re.I))
