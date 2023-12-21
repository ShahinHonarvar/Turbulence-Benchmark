
from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:7]
    palindromes = set()
    for i in range(4, len(string) + 1):
        for subset in permutations(string, i):
            subset = ''.join(subset).lower()
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
