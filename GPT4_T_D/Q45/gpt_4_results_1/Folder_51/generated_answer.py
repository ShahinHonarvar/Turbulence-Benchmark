
from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substr = string[3:6]

    palindromes = set()
    for i in range(3, len(substr)+1):
        for permutation in permutations(substr, i):
            cand = ''.join(permutation)
            if cand == cand[::-1] and len(cand) >= 3:
                palindromes.add(cand)
    return palindromes
