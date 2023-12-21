
import itertools

def palindromes_between_indices(string):
    letters = [char for char in string[1:7] if char.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    
    for permutation in itertools.permutations(unique_letters, len(letters)):
        word = ''.join(permutation).lower()
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
