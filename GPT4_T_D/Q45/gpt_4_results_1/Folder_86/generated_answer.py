
import itertools

def palindromes_between_indices(s):
    s = s[6:10].lower()
    perms = [''.join(p) for p in itertools.permutations(s)]
    return {p for p in perms if len(p) >= 4 and p == p[::-1]}
