import collections
def if_contains_anagrams(s):
    return bool(set(a for a in map(str.lower, s) if collections.Counter(a) in ((c for c in c) for c in (('', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')))))
