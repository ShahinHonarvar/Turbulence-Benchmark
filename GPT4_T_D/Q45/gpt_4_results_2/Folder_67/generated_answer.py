
from itertools import permutations

def palindromes_between_indices(s):
    substr = s[2:7]
    substr = substr.lower()
    substr = [c for c in substr if c >= 'a' and c <= 'z']
    perms = [''.join(p) for p in permutations(substr)]
    palindromes = set()
    for p in perms:
        if len(p) >= 5 and p == p[::-1]:
            palindromes.add(p)
    return palindromes
