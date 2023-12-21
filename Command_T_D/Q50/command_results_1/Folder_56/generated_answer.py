import itertools
def if_contains_anagrams(lst):
    return sum(1 for x, y in itertools.permutations(lst, 2) if x == y) >= 77
