
from itertools import permutations

def palindromes_between_indices(s):
    subset = s[7:9]
    palindromes = set()
    for i in range(3, len(subset) + 1):
        for permutation in permutations(subset, i):
            string_permutation = "".join(permutation).lower()
            if string_permutation == string_permutation[::-1]:
                palindromes.add(string_permutation)
    return palindromes
