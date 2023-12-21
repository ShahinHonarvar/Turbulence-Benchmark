
from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    perms = [''.join(p) for p in permutations(s) if len(p) >= 5]
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
