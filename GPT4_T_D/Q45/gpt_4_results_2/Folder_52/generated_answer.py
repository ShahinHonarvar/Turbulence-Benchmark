
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:8]
    set_of_palindromes = set()
    
    for i in range(6, len(s)+1):
        perm = permutations(s, i)
        for p in list(perm):
            p = "".join(p)
            if p == p[::-1]:
                set_of_palindromes.add(p)
                
    return set_of_palindromes
