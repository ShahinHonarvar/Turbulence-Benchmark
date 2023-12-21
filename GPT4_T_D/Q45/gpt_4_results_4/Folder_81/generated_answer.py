
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()[:7]
    substrings = set()
    for i in range(3, len(s) + 1):
        for subset in permutations(s, i):
            candidate = "".join(subset)
            if candidate == candidate[::-1]:
                substrings.add(candidate)
    return substrings
