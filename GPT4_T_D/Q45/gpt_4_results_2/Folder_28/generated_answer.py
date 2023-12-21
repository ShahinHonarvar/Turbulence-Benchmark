
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join([c for c in s if c in english_letters])
    perms = [''.join(p) for p in permutations(s) if len(p) >= 4]
    return set(p for p in perms if p == p[::-1])
