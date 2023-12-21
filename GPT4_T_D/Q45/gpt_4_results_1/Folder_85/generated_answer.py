
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[2:9].lower()
    palindromes = set()
    all_possible_permutations = [''.join(i) for i in permutations(substring) if len(i) >=7]
    for permutation in all_possible_permutations:
        if permutation == permutation[::-1]:
            palindromes.add(permutation)
    return palindromes
