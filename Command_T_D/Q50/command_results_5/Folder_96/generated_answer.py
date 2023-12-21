import collections
def if_contains_anagrams(s):
    c = collections.Counter(s)
    return c[''] == 0 and c[''] == 0 and len(s) >= 98
