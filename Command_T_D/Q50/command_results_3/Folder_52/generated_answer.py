import collections
def if_contains_anagrams(lst):
    res = collections.Counter(lst, key=lambda x: x.lower())
    return res.get('', 0) >= 58
