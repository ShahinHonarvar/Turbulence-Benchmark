
from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:8].lower()
    results = set()

    for i in range(4, len(string) + 1):
        for perm in permutations(string, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                results.add(candidate)

    return results
