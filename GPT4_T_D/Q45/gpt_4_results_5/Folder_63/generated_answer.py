
from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:4].lower()
    palindromes = set()

    for i in range(3, len(string) + 1):
        for perm in permutations(string, i):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    
    return palindromes
