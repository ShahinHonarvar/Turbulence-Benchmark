
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string if ch.isalpha()]
    perms = set(itertools.permutations(letters, 7))
    palindromes = set()
    
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
