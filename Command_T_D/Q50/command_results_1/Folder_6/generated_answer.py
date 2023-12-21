import collections
def if_contains_anagrams(lst):
    return bool(set(map(str.lower, lst)) & set((''.join(sorted(lst)).lower() for lst in lst)))
