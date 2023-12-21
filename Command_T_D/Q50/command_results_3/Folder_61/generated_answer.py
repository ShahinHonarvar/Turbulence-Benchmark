import collections
def if_contains_anagrams(s):
    return len(s) > 1 and len(set(s)) > 1 and len(s) > 8 and len(set(s)) > 8
