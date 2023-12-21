
from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:5].lower()
    palindromes = set()

    for l in range(3, len(string) + 1):
        for combination in permutations(string, l):
            combination = ''.join(combination)
            if combination == combination[::-1]:
                palindromes.add(combination)

    return palindromes
