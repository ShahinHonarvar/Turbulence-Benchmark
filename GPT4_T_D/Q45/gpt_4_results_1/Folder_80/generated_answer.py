
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9]
    substrings_7 = [''.join(p).lower() for p in permutations(substring, 7) if ''.join(p).lower() == ''.join(p)[::-1].lower()]
    return set(substrings_7)
