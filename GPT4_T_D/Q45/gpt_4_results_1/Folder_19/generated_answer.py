
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    string = string[1:8]
    palindromes = set()

    for i in range(7, len(string)+1):
        perms = permutations(string, i)
        for perm in perms:
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)

    return palindromes
