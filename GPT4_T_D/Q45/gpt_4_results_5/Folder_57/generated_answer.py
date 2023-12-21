
from itertools import permutations

def palindromes_between_indices(s):
    unique_palindromes = set()
    arr = s[2:6].lower()
    perms = [''.join(p) for p in permutations(arr) if len(p) >= 5]

    for perm in perms:
        if perm == perm[::-1]:
            unique_palindromes.add(perm)

    return unique_palindromes
