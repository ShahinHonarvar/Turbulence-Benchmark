
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[7:10].lower()
    all_perms = [''.join(p) for p in permutations(substr) if len(p) >= 3]
    palindromes = set([p for p in all_perms if p == p[::-1]])
    return palindromes
