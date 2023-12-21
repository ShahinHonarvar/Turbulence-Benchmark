
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    unique_perms = set([''.join(p) for p in permutations(s)])
    return {p for p in unique_perms if p == p[::-1] and len(p) >= 3}
