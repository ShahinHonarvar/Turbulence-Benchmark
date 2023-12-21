
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    char_perms = [''.join(p) for p in permutations(s) if len(p) >= 3]
    palindromes = set()
    for perm in char_perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
