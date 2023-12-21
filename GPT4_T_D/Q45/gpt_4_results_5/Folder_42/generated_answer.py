
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [c for c in s if c.isalpha()]
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 3]
    palindromes = {x for x in perms if x == x[::-1]}
    return palindromes
