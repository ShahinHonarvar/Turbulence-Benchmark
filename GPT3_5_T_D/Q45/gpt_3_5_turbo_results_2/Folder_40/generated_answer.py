
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    if len(english_letters) < 7 or len(english_letters[4:10]) < 7:
        return set()
    combinations = itertools.permutations(english_letters[4:10], 7)
    palindromes = set()
    for combo in combinations:
        if combo == combo[::-1]:
            palindromes.add(''.join(combo))
    return palindromes
