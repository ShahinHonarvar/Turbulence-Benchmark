
from itertools import permutations

def palindromes_between_indices(str_input):
    str_input = str_input[2:4]
    perms = [''.join(p) for p in permutations(str_input)]
    return set(word.lower() for word in perms if word.lower() == word.lower()[::-1] and len(word) >= 3)
