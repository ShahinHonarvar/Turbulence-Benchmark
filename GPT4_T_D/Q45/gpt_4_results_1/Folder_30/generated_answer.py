
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()[:5]
    palindromes = set()
    for p in permutations(s):
        candidate = ''.join(p)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
