
from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string[3:8].lower()
    perms = ["".join(p) for p in permutations(input_string)]
    return set(filter(lambda x: x == x[::-1] and len(x) >= 6, perms))
