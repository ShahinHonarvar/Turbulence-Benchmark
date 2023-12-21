import re
def if_contains_anagrams(texts):
    return bool(re.findall(r"(?i)(\S+)(?:-\d+)+", texts, flags=re.I))
