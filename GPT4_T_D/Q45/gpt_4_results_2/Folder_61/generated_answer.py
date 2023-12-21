
from itertools import permutations

def palindromes_between_indices(str):
    substring = str[0:8].lower()
    permuted_strings = set([''.join(p) for p in permutations(substring)])
    result = set()
    for s in permuted_strings:
        if s == s[::-1] and len(s) >= 7:
            result.add(s)
    return result
