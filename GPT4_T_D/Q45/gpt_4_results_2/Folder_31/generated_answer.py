
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    s = ''.join(ch for ch in s if ch.isalpha())
    all_perms = [''.join(p) for p in permutations(s)]
    return set(p for p in all_perms if len(p) >= 6 and p == p[::-1])
