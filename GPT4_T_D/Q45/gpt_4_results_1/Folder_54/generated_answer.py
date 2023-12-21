
from itertools import permutations

def palindromes_between_indices(string):
    string = string[4:10].lower()
    raw_perms = set([''.join(p) for p in permutations(string)])
    palindromes = set()
    for perm in raw_perms:
        if len(perm) >= 4 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
