import collections
def if_contains_anagrams(s):
    d = collections.Counter(w for w in s if len(w) >= 3)
    return d.get('*', 0) >= 79
