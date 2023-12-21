
from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:9].lower()
    palindromes = set()
    
    perms = [''.join(p) for p in permutations(string) if len(p) >= 5]
    
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    
    return palindromes
