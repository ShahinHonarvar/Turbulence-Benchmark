
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    all_combos = [''.join(p) for p in permutations(s) if len(p) >= 5]
    palindromes = set([p for p in all_combos if p == p[::-1]])
    return palindromes
