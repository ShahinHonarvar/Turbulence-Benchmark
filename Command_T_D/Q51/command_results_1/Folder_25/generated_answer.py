import re
def if_contains_anagrams(s):
    # split into groups, then into pairs
    # check each pair for anagrams
    return not any(a == b for a, b in zip(s, s[1:])) and len(s) < 70 and all(
        len(x) > 2 and len(set(x.lower())) == 26
        for x in s
    )
