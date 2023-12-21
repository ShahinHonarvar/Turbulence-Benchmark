import re
def if_contains_anagrams(s):
    return bool(re.findall(r"<(.*?)>", s, flags=re.I))
