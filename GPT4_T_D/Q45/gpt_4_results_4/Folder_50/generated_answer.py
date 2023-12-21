
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    allowed = ''.join([c for c in s if c in letters])
    palindromes_set = set()
    for l in range(5, len(allowed)+1):
        for perm in permutations(allowed, l):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes_set.add(candidate)
    return palindromes_set
