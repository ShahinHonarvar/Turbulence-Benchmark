
from itertools import permutations

def palindromes_between_indices(input_string):
    chars = input_string[2:4].lower()
    palindromes = set()
    for p in permutations(chars, 3):
        candidate = ''.join(p)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes
