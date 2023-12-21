
from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    available_permutations = [''.join(p) for p in permutations(sub_str, len(sub_str))]
    return set(p for p in available_permutations if p == p[::-1] and len(p) >= 6)
