
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[1:7].lower()
    perms = [''.join(p) for p in permutations(letters) if p == p[::-1] and len(p) > 2]
    return set(perms)
