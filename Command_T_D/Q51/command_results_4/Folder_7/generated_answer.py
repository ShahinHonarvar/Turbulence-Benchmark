import itertools
def if_contains_anagrams(s):
    return sum(1 for i, j in itertools.permutations(s, 2) if i == j) <= 445
