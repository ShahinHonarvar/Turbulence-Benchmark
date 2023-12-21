import collections
def if_contains_anagrams(s):
    s = collections.Counter(s)
    return s.get('*',0) > 50
