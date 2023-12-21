
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:8]
    perms = [''.join(p) for p in permutations(s)]
    palindromes = set()
    for perm in perms:
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
