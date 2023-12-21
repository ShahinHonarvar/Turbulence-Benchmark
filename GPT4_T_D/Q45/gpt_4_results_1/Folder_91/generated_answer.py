
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    chars = [c for c in s if c.isalpha()]
    perms = {"".join(p) for p in permutations(chars)}
    palindromes = {w for w in perms if w == w[::-1] and len(w) > 2}
    return palindromes
