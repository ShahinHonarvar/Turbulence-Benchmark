
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[5:10] if char.isalpha()]
    permutations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    
    for permutation in permutations:
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
