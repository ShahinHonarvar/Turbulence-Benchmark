
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for permutation in permutations(s, length):
            permutation_str = ''.join(permutation)
            if permutation_str == permutation_str[::-1]:
                palindromes.add(permutation_str)
    return palindromes
