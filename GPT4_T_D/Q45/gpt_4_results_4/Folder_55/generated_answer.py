
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:3].lower()
    perms = [''.join(p) for p in permutations(s) if len(p) >= 3]
    return {x for x in perms if x == x[::-1]}
