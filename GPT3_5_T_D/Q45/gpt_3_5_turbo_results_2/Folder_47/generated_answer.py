
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[3:8] if char.isalpha()]   
    permutations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    
    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
