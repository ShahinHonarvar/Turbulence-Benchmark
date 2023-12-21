
from itertools import permutations

def palindromes_between_indices(s):
    chars = list(s[3:7].lower())
    all_permutations = {"".join(p) for n in range(3, len(chars)+1) for p in permutations(chars, n)}
    return {p for p in all_permutations if p == p[::-1]}
