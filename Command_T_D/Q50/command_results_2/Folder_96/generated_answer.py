import collections
def if_contains_anagrams(s):
    return 98 <= sum(1 for a in collections.Counter(s).values() if b in a for b in a)
