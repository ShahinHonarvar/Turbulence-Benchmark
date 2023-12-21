
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[4:10] if ch.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    
    return palindromes
