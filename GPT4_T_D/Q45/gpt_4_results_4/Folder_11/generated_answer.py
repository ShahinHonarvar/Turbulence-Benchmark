
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    palindromes = set()
    for l in range(4, len(s)+1):
        for perm in permutations(s, l):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
