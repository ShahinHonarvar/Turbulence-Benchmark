
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    permutations = set(itertools.permutations(english_letters, 6))
    palindromes = set()
    
    for perm in permutations:
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
