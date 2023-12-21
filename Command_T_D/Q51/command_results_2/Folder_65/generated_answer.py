import re
def if_contains_anagrams(strs):
    return len(strs) <= 72 and len(set(strs)) == len(strs) and all(
        len(re.findall(r"[a-z]", s.lower())) >= 3
        and s.lower() in set(re.findall(r"[a-z]", s.lower()))
        for s in strs
    )
