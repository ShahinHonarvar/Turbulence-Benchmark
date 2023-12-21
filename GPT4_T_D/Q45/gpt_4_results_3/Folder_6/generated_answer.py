
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[0:8].lower()
    perm = [''.join(p) for p in permutations(letters) if len(p) >= 4]
    return set(x for x in perm if x == x[::-1])
