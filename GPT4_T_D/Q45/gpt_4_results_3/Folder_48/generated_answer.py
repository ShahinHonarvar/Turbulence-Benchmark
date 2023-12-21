
from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:9].lower()
    palindromes = set()
    
    possible_permutations = [''.join(p) for p in permutations(s) if len(p) >= 4]
    for p in possible_permutations:
        if p == p[::-1]:
            palindromes.add(p)

    return palindromes
