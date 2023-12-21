
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[7:10].lower()
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 3]
    return {p for p in perms if p == p[::-1]}
