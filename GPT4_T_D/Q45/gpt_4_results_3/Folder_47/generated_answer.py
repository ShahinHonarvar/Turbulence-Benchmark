
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:8].lower()
    unique_perms = set([''.join(p) for p in permutations(letters)])
    palindromes = set()
    for perm in unique_perms:
        if len(perm) >= 5 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
