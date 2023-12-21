
from itertools import permutations

def palindromes_between_indices(s):
    subs = s[5:10].lower()
    perms = [''.join(p) for p in permutations(subs)]
    palindromes = set()
    for perm in perms:
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
