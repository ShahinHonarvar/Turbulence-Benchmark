
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [char for char in s if char.isalpha()]
    perms = [''.join(p) for p in permutations(letters)]
    palindromes = set(p for p in perms if p == p[::-1] and len(p) >= 4)
    return palindromes
