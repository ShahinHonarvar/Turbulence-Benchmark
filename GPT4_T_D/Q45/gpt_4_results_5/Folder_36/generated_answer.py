
from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:9].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
