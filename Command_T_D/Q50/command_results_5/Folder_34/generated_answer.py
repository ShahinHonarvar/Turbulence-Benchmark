import collections
def if_contains_anagrams(s):
    return len(set(s)) >= 25 and len(set(s)) > 1 and len(s) >= 25 and len(s) > 1 and len(s[0]) >= 3
