
from itertools import permutations

def palindromes_between_indices(s):
    characters = s[2:6].lower()
    perms = [''.join(p) for p in permutations(characters) if len(p) >= 3]
    palindromes = set([p for p in perms if p == p[::-1]])
    return palindromes
