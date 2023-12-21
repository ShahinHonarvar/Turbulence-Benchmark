
from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:9].lower()
    palindromes = set()
    for i in range(4, len(string) + 1):
        for p in permutations(string, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
