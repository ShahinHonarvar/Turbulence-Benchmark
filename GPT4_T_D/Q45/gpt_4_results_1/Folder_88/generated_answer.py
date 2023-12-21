
from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s.lower()[3:8]
    s_set = set(s)
    all_combinations = []

    for i in range(6, len(s) + 1):
        combs = combinations(s_set, i)
        for comb in combs:
            perms = permutations(comb, i)
            all_combinations.extend([''.join(p) for p in perms])

    palindromes = set([pal for pal in all_combinations if pal == pal[::-1]])
    return palindromes
