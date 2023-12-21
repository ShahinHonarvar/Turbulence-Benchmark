
import itertools

def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(english_letters, 3):
        word = ''.join(permutation)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
