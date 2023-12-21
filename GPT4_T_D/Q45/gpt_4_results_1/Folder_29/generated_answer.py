
from itertools import permutations

def palindromes_between_indices(string):
    string = string[2:10].lower()
    all_palindromes = set()
    for i in range(6, len(string) + 1):
        for subset in permutations(string, i):
            subset = "".join(subset)
            if subset == subset[::-1]:
                all_palindromes.add(subset)
    return all_palindromes
