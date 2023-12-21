
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10]
    s = s.lower()
    all_perms = [''.join(p) for p in permutations(s)]
    palindromes = set()
    for perm in all_perms:
        if perm == perm[::-1] and len(perm) >= 4:
            palindromes.add(perm)
    return palindromes
