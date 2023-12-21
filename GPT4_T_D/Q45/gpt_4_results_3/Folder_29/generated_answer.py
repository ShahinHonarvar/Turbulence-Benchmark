
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[2:10]
    perms = [''.join(p) for p in permutations(substr) if len(p) >= 6]
    pali = [p for p in perms if p.lower() == p[::-1].lower()]
    return set(pali)
