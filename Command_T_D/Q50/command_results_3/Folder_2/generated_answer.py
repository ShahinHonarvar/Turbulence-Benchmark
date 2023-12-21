import re
def if_contains_anagrams(s):
    return bool(re.findall(r'\A(?!\d)\w{3,}(?!\d)\w{3,}\Z', s, flags=re.I))
