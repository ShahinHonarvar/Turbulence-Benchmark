
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for perm in permutations(s[0:5]):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            palindromes.add(candidate)
    return palindromes
