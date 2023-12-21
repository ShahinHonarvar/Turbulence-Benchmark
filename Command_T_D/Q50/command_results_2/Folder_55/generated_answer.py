import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\s).*', s, flags=re.I))
