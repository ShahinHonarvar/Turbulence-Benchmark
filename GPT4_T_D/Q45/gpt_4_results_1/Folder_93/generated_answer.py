
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8]
    palindromes = set()

    for i in range(6, len(substring)+1):
        for perm in permutations(substring, i):
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)

    return palindromes
