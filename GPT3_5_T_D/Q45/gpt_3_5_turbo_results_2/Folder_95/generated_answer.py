
import itertools

def palindromes_between_indices(string):
    english_letters = []
    for char in string[7:9]:
        if char.isalpha():
            english_letters.append(char.lower())
    combinations = itertools.permutations(english_letters, 3)
    palindromes = set()
    for combo in combinations:
        if combo == combo[::-1]:
            palindromes.add(''.join(combo))
    return palindromes
