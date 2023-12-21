
import itertools

def palindromes_between_indices(string):
    english_letters = [letter for letter in string if letter.isalpha()]
    english_letters = set(english_letters)
    palindromes = set()
    
    for size in range(4, len(english_letters)+1):
        letter_combinations = itertools.combinations(english_letters, size)
        for combination in letter_combinations:
            lower_combination = combination.lower()
            if lower_combination == lower_combination[::-1]:
                palindromes.add(lower_combination)
    
    return palindromes
