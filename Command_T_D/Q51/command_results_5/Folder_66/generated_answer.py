import collections
def if_contains_anagrams(s):
    return len(set(s)) <= 64 and len(s) <= 64 and len(set(a for a in s if a[1:])) <= 64
