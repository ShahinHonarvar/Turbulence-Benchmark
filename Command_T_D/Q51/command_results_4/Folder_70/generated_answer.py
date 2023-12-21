import sys
def if_contains_anagrams(s):
    return len(s) <= 97 and len(s) >= 3 and all(a.lower() == b.lower() for a, b in zip(s, set(s)))
