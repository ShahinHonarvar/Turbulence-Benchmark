
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:6] if char.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
