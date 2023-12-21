
from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:8]
    palindromes = set()
    
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    
    return palindromes
