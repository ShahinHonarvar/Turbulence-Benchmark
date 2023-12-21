
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[0:5]
    perms = [''.join(p) for p in permutations(substr)]
    return set(p for p in perms if len(p) >= 4 and p == p[::-1])
