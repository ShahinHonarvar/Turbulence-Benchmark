
from itertools import permutations

def palindromes_between_indices(s):     
    sub_str = s[7:10].lower()
    palindromes = set()
    
    perms = [''.join(p) for p in permutations(sub_str) if len(p) >= 3]
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
            
    return palindromes
