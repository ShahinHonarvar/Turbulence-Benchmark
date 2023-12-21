
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    english_letters = [char for char in string if char.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(english_letters, 3):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
