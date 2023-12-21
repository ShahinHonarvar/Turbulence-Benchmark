
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    palindromes = set()
    for i in range(6, len(s) + 1):
        for perm in permutations(s, i):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes
