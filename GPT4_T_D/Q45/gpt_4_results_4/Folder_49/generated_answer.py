
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[5:8].lower()
    all_perms = set([''.join(p) for p in permutations(subset) if len(p) >= 3])
    palindromes = {word for word in all_perms if word == word[::-1]}
    return palindromes
