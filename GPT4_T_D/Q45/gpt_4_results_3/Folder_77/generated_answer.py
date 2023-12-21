
from itertools import permutations

def palindromes_between_indices(s):
    subs = s[4:7]
    perms = [''.join(p) for p in permutations(subs) if len(p) >= 4]
    return set(x for x in perms if x.lower() == x[::-1].lower())
