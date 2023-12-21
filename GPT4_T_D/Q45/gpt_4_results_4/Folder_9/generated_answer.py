
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[:7]
    perm = [''.join(p) for p in permutations(s)]
    perm = set([x for x in perm if len(x) >= 7])
    palindromes = set([x for x in perm if x == x[::-1]])
    return palindromes
