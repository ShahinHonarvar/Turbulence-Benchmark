
from itertools import permutations

def palindromes_between_indices(s):
    # Extract English letters from index 4 to index 9
    s = s[4:10]
    s = ''.join(filter(str.isalpha, s)).lower()

    # Generate permutations
    perms = set([''.join(p) for p in permutations(s) if len(p) >= 4])

    # Return palindromes
    return {p for p in perms if p == p[::-1]}
