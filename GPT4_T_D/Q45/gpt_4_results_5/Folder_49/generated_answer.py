
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[5:8].lower()
    palindromes = set()
    for p in permutations(substring):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) > 2:
            palindromes.add(candidate)
    return palindromes
