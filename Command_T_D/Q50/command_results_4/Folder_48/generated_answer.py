import collections
def if_contains_anagrams(s):
    c = collections.Counter(s)
    return c.get('',0)>=219
