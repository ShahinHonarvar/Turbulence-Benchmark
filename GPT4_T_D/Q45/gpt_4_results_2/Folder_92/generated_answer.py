
from itertools import permutations

def palindromes_between_indices(text):
    text = text[4:8].lower()
    results = set()
    for length in range(4, len(text) + 1):
        for perm in permutations(text, length):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                results.add(perm)
    return results
