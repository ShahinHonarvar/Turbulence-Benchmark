
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    combinations = set(itertools.combinations(english_letters, 6))
    palindromes = set()
    for combination in combinations:
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
