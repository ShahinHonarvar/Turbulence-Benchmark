
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[1:5] if ch.isalpha()]
    perms = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    
    for perm in perms:
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
