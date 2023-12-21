
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:4].lower()
    all_combinations = set([''.join(p) for p in permutations(s) if len(p) >= 3])
    return set([word for word in all_combinations if word == word[::-1]])
