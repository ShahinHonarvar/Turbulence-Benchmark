
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:4]
    s = s.lower()
    results = set()
    for length in range(4, len(s) + 1):
        for subset in permutations(s, length):
            candidate = "".join(subset)
            if candidate == candidate[::-1]:
                results.add(candidate)
    return results
