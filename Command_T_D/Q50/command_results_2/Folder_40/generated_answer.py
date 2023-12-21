import re
def if_contains_anagrams(s):
    return len(s) >= 3 and any(a == b for a, b in zip(s, s)) and any(a == b for a, b in zip(s, s))
