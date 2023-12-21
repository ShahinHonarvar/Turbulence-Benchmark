
import itertools

def palindromes_between_indices(string):
    substring = string[8:10].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters, len(letters)):
        word = "".join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
