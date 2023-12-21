
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    possible_combinations = [''.join(p) for p in permutations(s[1:3])]
    return set(word for word in possible_combinations if len(word) >= 3 and word == word[::-1])
