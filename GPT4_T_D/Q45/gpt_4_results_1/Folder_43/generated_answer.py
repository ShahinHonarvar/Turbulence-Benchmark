
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[2:6].lower()
    perms = [''.join(p) for p in permutations(subset)]
    return set(p for p in perms if p == p[::-1] and len(p) >= 4)
