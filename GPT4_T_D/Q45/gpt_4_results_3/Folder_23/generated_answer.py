
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for size in range(4, 8):
        for permutation in permutations(string[:7], size):
            candidate = "".join(permutation)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
