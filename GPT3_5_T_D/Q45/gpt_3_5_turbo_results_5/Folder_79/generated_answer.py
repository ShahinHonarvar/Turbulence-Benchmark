
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[1:8] if ch.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
