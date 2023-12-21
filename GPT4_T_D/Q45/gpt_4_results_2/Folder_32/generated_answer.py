
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    relevant_chars = s[1:8]
    perms = [''.join(p) for p in permutations(relevant_chars)]
    
    return {p for p in perms if len(p) >= 5 and p == p[::-1]}
