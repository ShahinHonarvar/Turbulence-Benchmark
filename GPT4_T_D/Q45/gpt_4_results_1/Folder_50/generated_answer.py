
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[4:9].lower()
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
