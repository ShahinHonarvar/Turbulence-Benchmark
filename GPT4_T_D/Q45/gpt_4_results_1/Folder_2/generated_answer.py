
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    palindromes = set()
    
    unique_perms = set(permutations(s))
    
    for perm in unique_perms:
        perm_s = ''.join(perm)
        if len(perm_s) >= 6 and perm_s == perm_s[::-1]:
            palindromes.add(perm_s)
    
    return palindromes
