
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    unique_permutations = set(["".join(p) for p in permutations(s)])
    palindromes = {p for p in unique_permutations if len(p) >= 4 and p == p[::-1]}
    return palindromes
