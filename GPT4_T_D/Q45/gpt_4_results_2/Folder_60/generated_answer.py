
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    perms = [''.join(p) for p in permutations(s) if len(p) >= 4]
    palindromes = set([p for p in perms if p == p[::-1]])
    return palindromes
