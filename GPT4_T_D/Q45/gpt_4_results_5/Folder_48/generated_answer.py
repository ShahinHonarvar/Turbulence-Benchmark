
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[6:9].lower()
    permuts = [''.join(p) for p in permutations(substr) if len(p) >= 4]
    return set(p for p in permuts if p == p[::-1])
