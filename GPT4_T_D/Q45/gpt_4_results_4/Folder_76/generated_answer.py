
from itertools import permutations

def palindromes_between_indices(s):
    indices_str = s[1:5].lower()
    possible_pals = set([''.join(p) for p in permutations(indices_str) if len(p) >= 4 and ''.join(p) == ''.join(p)[::-1]])
    return possible_pals
