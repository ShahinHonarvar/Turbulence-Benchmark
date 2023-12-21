import re
def if_contains_anagrams(s):
    s = sorted(s)
    return all(x != y for x, y in zip(s, s[1:]) if len(x) >= 3 and len(y) >= 3 and x != y)
