
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    chars = [char for char in s if char.isalpha()]
    perms = [''.join(p) for p in permutations(chars) if len(p) >= 5]
    return set(perm for perm in perms if perm == perm[::-1])
