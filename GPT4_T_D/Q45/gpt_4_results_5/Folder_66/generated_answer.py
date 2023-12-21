
from itertools import permutations

def palindromes_between_indices(string):
    if len(string) < 5:
        return set()

    substring = string[0:6].lower()
    palindromes = set()

    for i in range(5, len(substring) + 1):
        for perm in permutations(substring, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)

    return palindromes
