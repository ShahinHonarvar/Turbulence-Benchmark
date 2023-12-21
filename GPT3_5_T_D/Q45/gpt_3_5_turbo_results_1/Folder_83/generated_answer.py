
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    possibilities = set(itertools.permutations(letters, 8))
    palindromes = set()
    for possibility in possibilities:
        word = "".join(possibility)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
