
from itertools import permutations

def palindromes_between_indices(input_string):
    permutes = set()
    input_string = input_string[0:4]
    for i in range(4, len(input_string) + 1):
        permutes.update([''.join(p).lower() for p in permutations(input_string, i) if ''.join(p).lower() == ''.join(p).lower()[::-1]])
    return permutes
