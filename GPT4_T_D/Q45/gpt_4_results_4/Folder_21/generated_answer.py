
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    palindromes = set()

    for length in range(7, len(s) + 1):
        for permutation in permutations(s, length):
            perm_str = ''.join(permutation)

            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)

    return palindromes
