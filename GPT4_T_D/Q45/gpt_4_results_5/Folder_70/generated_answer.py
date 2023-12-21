
from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[1:7].lower()
    perms = [''.join(p) for p in permutations(sub_s)]
    return set(p for p in perms if len(p) >= 4 and p == p[::-1])
