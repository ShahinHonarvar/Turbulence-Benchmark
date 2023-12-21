
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:4].lower()
    perms = [''.join(p) for p in permutations(s)]
    return set(p for p in perms if len(p) >= 4 and p == p[::-1])
