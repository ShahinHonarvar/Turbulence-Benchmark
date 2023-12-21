
from itertools import permutations

def palindromes_between_indices(str):
    str = str[2:6].lower()
    substrings = [''.join(p) for p in permutations(str) if p == p[::-1] and len(p) >= 4]
    return set(substrings)
