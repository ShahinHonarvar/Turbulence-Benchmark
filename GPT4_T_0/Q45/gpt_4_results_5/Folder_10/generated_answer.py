
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for perm in permutations(s, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
