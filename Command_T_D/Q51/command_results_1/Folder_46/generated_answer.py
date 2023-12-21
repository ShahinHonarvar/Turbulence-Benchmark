import collections
def if_contains_anagrams(lst):
    return sum(1 for s in lst if s in collections.Counter(s.lower())) <= 60
