
from itertools import permutations

def palindromes_between_indices(str):
    str = str.lower()
    sub_str = str[3:10]
    perms = [''.join(p) for p in permutations(sub_str)]
    filtered_perms = [perm for perm in perms if len(perm) >= 7 and perm == perm[::-1]]
    return set(filtered_perms)
