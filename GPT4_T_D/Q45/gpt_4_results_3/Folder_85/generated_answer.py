
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[2:9]
    palindromes = set()
    for i in range(7, len(substr)+1):
        perms = [''.join(p).lower() for p in permutations(substr, i)]
        for perm in perms:
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes
