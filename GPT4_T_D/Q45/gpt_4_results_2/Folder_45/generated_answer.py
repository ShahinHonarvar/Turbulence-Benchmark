
from itertools import permutations

def palindromes_between_indices(string):
    string = string[5:10].lower()
    palindromes = set()
    for i in range(4, len(string) + 1):
        for combination in permutations(string, i):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
