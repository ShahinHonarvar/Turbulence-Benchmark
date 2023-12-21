
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:4].lower()
    unique_permutations = set("".join(p) for p in permutations(s))
    palindromes = {p for p in unique_permutations if p == p[::-1] and len(p) >= 3}

    return palindromes
