
from itertools import permutations

def palindromes_between_indices(given_string):
    selection = given_string[3:9].replace(" ", "").lower()
    perms = [''.join(p) for p in permutations(selection) if len(p) >= 4]
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes
