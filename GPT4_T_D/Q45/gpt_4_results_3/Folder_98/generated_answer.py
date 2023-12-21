
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[3:6].lower()
    
    perms = [''.join(p) for p in permutations(sub_string) if len(p) >= 4]
    palindromes = set([p for p in perms if p == p[::-1]])
    
    return palindromes
