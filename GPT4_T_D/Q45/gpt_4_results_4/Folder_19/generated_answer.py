
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    all_perms = [''.join(p) for p in permutations(s, len(s))]
    palindromes = set([p for p in all_perms if p == p[::-1] and len(p) >= 7])
    return palindromes
