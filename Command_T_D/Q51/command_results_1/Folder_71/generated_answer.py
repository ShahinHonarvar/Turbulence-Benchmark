import collections
def if_contains_anagrams(s):
    d = collections.Counter(s)
    return all(a == b for a, b in zip(s, s)) and len(s) <= 9
