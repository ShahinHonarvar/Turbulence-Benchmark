
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    all_permutations = set()
    for n in range(5, len(s) + 1):
        all_permutations.update(["".join(p) for p in permutations(s, n)])
    return {p for p in all_permutations if p == p[::-1]}
