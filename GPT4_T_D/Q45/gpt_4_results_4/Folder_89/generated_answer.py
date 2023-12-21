
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[5:10]
    palindromes = set()
    for length in range(6, len(s)+1):
        for perm in permutations(s, length):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes
