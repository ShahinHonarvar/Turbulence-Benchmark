
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = s[0:4]
    perms = [''.join(p) for p in permutations(chars) if len(p) > 3]
    palindrome_perms = {p for p in perms if p == p[::-1]}
    return palindrome_perms
