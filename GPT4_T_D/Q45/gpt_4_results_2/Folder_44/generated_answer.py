
from itertools import permutations

def palindromes_between_indices(string):
    chars = string[2:8].lower()
    unique_perms = set([''.join(p) for p in permutations(chars) if p == p[::-1] and len(p) >= 3])
    return unique_perms
