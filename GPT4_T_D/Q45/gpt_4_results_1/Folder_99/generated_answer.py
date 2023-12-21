
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = [char for char in s if char.isalpha()]
    perms = [''.join(p) for p in permutations(letters) if len(p) >= 3]
    palindromes = set([p for p in perms if p == p[::-1]])
    return palindromes
