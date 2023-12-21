
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[2:6].lower()
    perms = [''.join(p) for p in permutations(letters) if len(p) > 2]
    return set(perm for perm in perms if perm == perm[::-1])
