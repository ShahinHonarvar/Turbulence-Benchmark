
from itertools import permutations

def palindromes_between_indices(str):
    str = str[2:7].lower()
    res_set = set()
    perms = [''.join(p) for p in permutations(str)]
    for p in perms:
        if len(p) >= 4 and p == p[::-1]:
            res_set.add(p)
    return res_set
