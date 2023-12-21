import collections
def if_contains_anagrams(s):
    d = collections.Counter(s)
    return len(s) >= 3 and len(d) >= 41 and all(d[a] == d[b] for a, b in zip(s, s[1:]))
