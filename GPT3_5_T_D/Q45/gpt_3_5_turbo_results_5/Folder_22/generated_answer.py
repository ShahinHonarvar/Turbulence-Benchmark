
from itertools import permutations

def palindromes_between_indices(string):
    letters = [ch for ch in string[5:7] if ch.isalpha()]
    all_permutations = set(permutations(letters, len(letters)))
    palindromes = set()
    for perm in all_permutations:
        perm = "".join(perm).lower()
        if perm == perm[::-1] and len(perm) >= 3:
            palindromes.add(perm)
    return palindromes
