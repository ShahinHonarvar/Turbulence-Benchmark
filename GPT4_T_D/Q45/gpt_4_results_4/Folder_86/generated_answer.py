
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    perms = [''.join(p) for p in permutations(substring) if len(p) >= 4]
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes
