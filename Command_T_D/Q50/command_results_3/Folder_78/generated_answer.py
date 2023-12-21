import collections
def if_contains_anagrams(s):
    d = collections.Counter(s)
    return len(d) > 78
