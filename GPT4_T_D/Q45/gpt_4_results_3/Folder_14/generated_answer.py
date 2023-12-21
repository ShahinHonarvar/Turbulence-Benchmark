
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:6]
    palindromes = set()
    
    for i in range(3, len(s)+1):
        for perm in permutations(s, i):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
                
    return palindromes
