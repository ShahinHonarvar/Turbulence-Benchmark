
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    perms = [''.join(p) for p in permutations(s)]
    palindromes = {p for p in perms if p == p[::-1] and len(p)>=3}
    return palindromes
