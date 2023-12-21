
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8].lower()
    perms = [''.join(p) for p in permutations(letters) if ''.join(p)[::-1] == ''.join(p) and len(''.join(p)) >= 4]
    return set(perms)
