import collections
def if_contains_anagrams(s):
    return len(s) <= 97 and len(s) > 2 and len(s) == len(set(s)) and all(a == b for a, b in zip(s, sorted(s)))
