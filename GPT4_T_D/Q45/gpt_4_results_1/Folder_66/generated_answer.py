
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_str = s[:6]
    perms = [''.join(p) for p in permutations(sub_str)]
    palindromes = set()
    for perm in perms:
        if len(perm) > 4 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
