
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    letters_between_indices = english_letters[4:10]
    permutations = list(itertools.permutations(letters_between_indices, len(letters_between_indices)))

    palindromes = set()
    for perm in permutations:
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
