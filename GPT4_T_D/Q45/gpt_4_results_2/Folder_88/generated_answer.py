
from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    s = s[3:8].lower()
    for length in range(6, len(s) + 1):
        for perm in permutations(s, length):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm) 
    return palindromes
