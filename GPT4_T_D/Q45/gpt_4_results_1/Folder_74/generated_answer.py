
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[1:7]
    palindromes = set()
    
    for i in range(3, len(s) + 1):
        perms = permutations(s, i)
        for perm in perms:
            candidate = "".join(perm)
            if candidate == candidate[::-1] and len(candidate) >= 6:
                palindromes.add(candidate)
    
    return palindromes
