
from itertools import permutations
  
def palindromes_between_indices(s):
    s = s[2:6].lower()
    perms = [''.join(p) for p in permutations(s)]
    return set([per for per in perms if len(per) >= 5 and per == per[::-1]])
