
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower() 
    return set(''.join(p) for p in permutations(s) if len(p) >= 3 and ''.join(p) == ''.join(p)[::-1])
