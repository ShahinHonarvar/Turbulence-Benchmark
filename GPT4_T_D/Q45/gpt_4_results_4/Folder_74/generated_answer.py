
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    perms = ["".join(p) for p in permutations(s)]
    for perm in perms:
        if perm == perm[::-1] and len(perm) >= 6:
            palindromes.add(perm)
    return palindromes
