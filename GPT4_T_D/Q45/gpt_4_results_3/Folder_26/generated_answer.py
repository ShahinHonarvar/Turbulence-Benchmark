
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:7].lower()
    palindromes = set()
    for i in range(3, len(substr) + 1):
        perms = permutations(substr, i)
        for perm in perms:
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
