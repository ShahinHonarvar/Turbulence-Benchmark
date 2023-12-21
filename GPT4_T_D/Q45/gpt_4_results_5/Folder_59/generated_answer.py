
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[8:10]
    perms = [''.join(p) for p in permutations(subset)]
    return set([p.lower() for p in perms if p.lower() == p[::-1].lower() and len(p) >= 3])
