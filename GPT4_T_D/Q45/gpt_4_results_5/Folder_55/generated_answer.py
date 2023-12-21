
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    sub_string = string[0:3]
    palindromes = set()
    perms = [''.join(p) for p in permutations(sub_string)]
    for perm in perms:
        if perm == perm[::-1] and len(perm) >= 3:
            palindromes.add(perm)
    return palindromes
