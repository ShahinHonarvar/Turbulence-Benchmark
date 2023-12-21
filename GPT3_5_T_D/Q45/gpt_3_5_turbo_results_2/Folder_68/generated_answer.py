
import itertools


def palindromes_between_indices(string):
    letters = ''.join(c for c in string if c.isalpha())
    letters = letters[1:9].lower()
    palindromes = set()
    
    for combination in itertools.permutations(letters, len(letters)):
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
