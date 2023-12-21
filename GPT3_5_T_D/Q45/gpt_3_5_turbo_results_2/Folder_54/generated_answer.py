
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:10] if char.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, len(letters)):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
