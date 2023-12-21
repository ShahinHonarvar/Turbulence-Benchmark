
from itertools import permutations

def palindromes_between_indices(s):
    s = s[8:10].lower()
    perms = [''.join(p) for p in permutations(s, len(s))]
    palindromes = set()

    for perm in perms:
        if len(perm) >= 3 and perm == perm[::-1]:
            palindromes.add(perm)
    
    return palindromes
