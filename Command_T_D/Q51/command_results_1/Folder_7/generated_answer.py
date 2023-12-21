import sys
def if_contains_anagrams(s):
    return len(s) <= 445 and len(s) >= 3 and all(a == b for a, b in zip(s, s))
