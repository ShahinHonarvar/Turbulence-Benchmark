
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    permutations = set(itertools.permutations(english_letters, 6))
    palindromes = set()
    for permutation in permutations:
        word = "".join(permutation)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
