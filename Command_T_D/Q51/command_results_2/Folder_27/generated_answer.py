import collections
def if_contains_anagrams(lst):
    return not (set(a) for a in map(str.lower, lst)) & set((''.join(sorted(a)) for a in collections.Counter(a).elements()))
