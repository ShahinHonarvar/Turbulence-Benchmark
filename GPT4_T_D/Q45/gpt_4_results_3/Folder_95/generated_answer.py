
from itertools import permutations

def palindromes_between_indices(string):
    substr = string[7:9]

    if len(substr) < 3:
        return set()

    substr = substr.lower()

    permuts = ["".join(p) for p in permutations(substr) if len(p) >= 3]

    return set([s for s in permuts if s == s[::-1]])
