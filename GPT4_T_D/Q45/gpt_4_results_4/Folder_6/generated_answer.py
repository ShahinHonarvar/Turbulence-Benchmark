
from itertools import permutations

def palindromes_between_indices(s):
    chars_extracted = s[0:8]
    chars_lowercase = chars_extracted.lower()
    perms = [''.join(p) for p in permutations(chars_lowercase) if len(p) >= 4]
    return set(p for p in perms if p == p[::-1])
