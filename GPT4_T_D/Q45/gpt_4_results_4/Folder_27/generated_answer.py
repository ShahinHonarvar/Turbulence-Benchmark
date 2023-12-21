
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    s_set = set()
    for i in range(6, len(s) + 1):
        perms = [''.join(p) for p in permutations(s, i)]
        for perm in perms:
            if perm == perm[::-1]:
                s_set.add(perm)
    return s_set
