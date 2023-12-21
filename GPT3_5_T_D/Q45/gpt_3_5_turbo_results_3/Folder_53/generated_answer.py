
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    combinations = set(itertools.permutations(english_letters, len(english_letters)))
    palindromes = set()
    for combination in combinations:
        substring = ''.join(combination[4:9]).lower()
        if substring == substring[::-1] and len(substring) >= 6:
            palindromes.add(substring)
    return palindromes
