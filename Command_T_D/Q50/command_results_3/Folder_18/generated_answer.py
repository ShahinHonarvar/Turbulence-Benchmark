import collections
def if_contains_anagrams(s):
    return len(set(a for a in collections.Counter(s).values() if len(a)>=3))>1000000
