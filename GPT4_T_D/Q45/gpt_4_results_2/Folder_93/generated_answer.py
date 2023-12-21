
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    chars = [ch for ch in s if ch.isalpha()]
    perms = set()
    for perm in permutations(chars):
        s = ''.join(perm)
        perms.add(s)
    return set(s for s in perms if len(s) >= 6 and s == s[::-1])
