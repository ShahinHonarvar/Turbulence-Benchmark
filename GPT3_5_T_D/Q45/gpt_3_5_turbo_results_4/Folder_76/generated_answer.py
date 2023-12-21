
import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()

    for combination in itertools.permutations(letters, 4):
        word = ''.join(combination).lower()
        if word == word[::-1]:
            palindromes.add(word)

    return palindromes
