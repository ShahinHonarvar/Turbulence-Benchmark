
from itertools import permutations

def palindromes_between_indices(s):
    char_range = s[5:7]
    length = len(char_range)
    if length < 3:
        return set()

    char_range = char_range.lower()
    perms = set([''.join(p) for p in permutations(char_range)])
    return {p for p in perms if p == p[::-1] and len(p) >= 3}
