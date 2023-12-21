
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:7]
    results = set()
    for i in range(6, len(s) + 1):
        for perm in permutations(s, i):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                results.add(candidate)
    return results
