
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    english_letters = english_letters[5:10]
    combinations = list(itertools.permutations(english_letters))
    palindromes = set()
    for comb in combinations:
        if comb == comb[::-1]:
            palindromes.add(''.join(comb))
    return palindromes
