
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    s = ''.join(filter(str.isalpha, s))
    perms = set([''.join(p) for p in permutations(s) if len(set(p)) >= 5])
    return set(filter(lambda x: x == x[::-1], perms))
