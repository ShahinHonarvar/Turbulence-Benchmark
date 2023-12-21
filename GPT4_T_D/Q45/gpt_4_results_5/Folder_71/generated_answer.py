
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:4].lower()
    perms = {''.join(p) for p in permutations(s) if len(p) >= 4}
    return {p for p in perms if p == p[::-1]}
