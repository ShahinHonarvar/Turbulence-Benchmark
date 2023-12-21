
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    perms = [''.join(p) for p in permutations(s) if len(p) >= 4]
    return set(p for p in perms if p == p[::-1])
