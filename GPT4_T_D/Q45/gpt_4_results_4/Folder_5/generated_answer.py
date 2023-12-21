
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:9].lower()
    perms = [''.join(p) for p in permutations(letters)]
    return {p for p in perms if len(p) >= 4 and p == p[::-1]}
