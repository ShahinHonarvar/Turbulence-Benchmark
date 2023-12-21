
from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    unique_combinations = set(combinations(s, 6))
    pallindromes = set()
    for combination in unique_combinations:
        all_permutations = set(permutations(combination, 6))
        for permut in all_permutations:
            word = "".join(permut)
            if word == word[::-1]:
                pallindromes.add(word)
    return pallindromes
