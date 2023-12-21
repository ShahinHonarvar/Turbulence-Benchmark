
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:6]
    palin_set = set()
    for i in range(6, len(s) + 1):
        perms = [''.join(p) for p in permutations(s,i)]
        for perm in perms:
            if perm == perm[::-1]:
                palin_set.add(perm)
    return palin_set
