
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:6] if char.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
