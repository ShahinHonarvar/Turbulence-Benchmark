import re
def if_contains_anagrams(texts):
    return bool(re.findall(r"((?i)([A-Z])\2)", texts, flags=re.I))
