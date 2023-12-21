
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7]
    palindromes = set()

    for length in range(3, len(substring) + 1):
        perms = map("".join, permutations(substring, length))
        for perm in perms:
            if perm.lower() == perm.lower()[::-1]:
                palindromes.add(perm)

    return palindromes
