
import itertools

def palindromes_between_indices(s):
    s = s[2:5].lower()
    perms = set([''.join(p) for p in itertools.permutations(s)])
    return set([p for p in perms if len(p) >= 4 and p == p[::-1]])
