
from itertools import permutations

def palindromes_between_indices(s):
    chars = s[3:9]
    palindromes = set()
    for i in range(4, len(chars) + 1):
        perms = permutations(chars, i)
        for perm in perms:
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
