
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[:7]
    perms = permutations(substr)
    palindromes = set()
    for p in perms:
        p_str = "".join(p)
        if p_str == p_str[::-1] and len(p_str) >= 3:
            palindromes.add(p_str)
    return palindromes
