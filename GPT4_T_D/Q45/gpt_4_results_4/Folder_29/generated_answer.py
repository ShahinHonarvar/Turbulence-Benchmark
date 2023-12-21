
from itertools import permutations

def palindromes_between_indices(string):
    subset = string[2:10].lower()
    palindromes = set()
    for i in range(6, len(subset) + 1):
        perms = [''.join(p) for p in permutations(subset, i)]
        for perm in perms:
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes
