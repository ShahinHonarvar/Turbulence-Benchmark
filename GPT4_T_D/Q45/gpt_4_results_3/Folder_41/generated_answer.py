
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:4].lower()
    perms = [''.join(p) for p in permutations(s)]
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1] and len(perm) >= 3:
            palindromes.add(perm)
    return palindromes
