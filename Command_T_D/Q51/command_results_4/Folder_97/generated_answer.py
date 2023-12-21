import re
def if_contains_anagrams(s):
    #your code here
    return bool(re.findall(r"((?:[a-z]){3})\1", s, flags=re.I))
