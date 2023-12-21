
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    unique_perms = set(''.join(p) for p in permutations(s) if len(p) >= 3)
    return {p for p in unique_perms if p == p[::-1]}
