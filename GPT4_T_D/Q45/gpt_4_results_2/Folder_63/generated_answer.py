
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for n in range(3, len(s) + 1):
        for perm in permutations(s, n):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
