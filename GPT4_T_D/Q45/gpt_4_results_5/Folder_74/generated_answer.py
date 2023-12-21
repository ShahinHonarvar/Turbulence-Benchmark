
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[1:7]
    palindromes = set()
    for length in range(6, len(substring)+1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
