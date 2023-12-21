import collections
def if_contains_anagrams(s):
    return all(a!=b for a,b in collections.Counter(a).items() for a,b in collections.Counter(b).items() if a==b)
