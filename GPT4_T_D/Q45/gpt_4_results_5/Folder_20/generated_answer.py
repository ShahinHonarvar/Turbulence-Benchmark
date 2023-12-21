
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9]
    palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in permutations(s, i):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
