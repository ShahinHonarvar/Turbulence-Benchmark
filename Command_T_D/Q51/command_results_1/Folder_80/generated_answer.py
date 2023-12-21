import collections
def if_contains_anagrams(s):
    return len(set(s)) <= 255 and len(set(s)) > 0 and all(a == b for a, b in zip(s, s))
