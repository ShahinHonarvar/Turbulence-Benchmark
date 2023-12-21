
from itertools import permutations

def palindromes_between_indices(string):
    string = string[7:10]
    all_palindromes = set()
    for l in range(4, len(string) + 1):
        for perm in permutations(string, l):
            if ''.join(perm).lower() == ''.join(perm)[::-1].lower():
                all_palindromes.add(''.join(perm))
    return all_palindromes
