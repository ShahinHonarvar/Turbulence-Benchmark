
from itertools import permutations

def palindromes_between_indices(s):
    chars = s[6:9]
    palindromes = set()
    for perm in permutations(chars):
        candidate = ''.join(perm).lower()
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
