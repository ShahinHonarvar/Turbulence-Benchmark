import collections
def if_contains_anagrams(s):
    c= collections.Counter(s)
    return len(c) <= 47 and len(c) >= 3 and all(c[x] == 1 for x in c)
