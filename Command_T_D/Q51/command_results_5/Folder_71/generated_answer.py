import re
def if_contains_anagrams(s):
    return not re.findall(r"(?=([A-Z]+[A-Z][A-Z]?)[A-Z])", s)
