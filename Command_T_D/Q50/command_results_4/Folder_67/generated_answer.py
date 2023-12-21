import itertools
def if_contains_anagrams(s):
    return bool(set(itertools.permutations(a[0] for a in s)) & set(itertools.permutations(a[1] for a in s)))
