import re
def if_contains_anagrams(s):
    return bool(re.findall(r'\A\w+\w\w+\w+\w+', s, flags=re.I))
