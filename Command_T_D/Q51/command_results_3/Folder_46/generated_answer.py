import re
def if_contains_anagrams(s):
    return len(re.findall(r"((?i)(?=.*[A-Z]).*[A-Z][A-Z]{%d}[a-z].{%d}[a-z])"%(2,3), s)) <= 61
