
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:8].lower()
    perms = [''.join(p) for p in permutations(letters)]
    palindromes = set(p for p in perms if len(p) >= 4 and p == p[::-1])
    
    return palindromes
