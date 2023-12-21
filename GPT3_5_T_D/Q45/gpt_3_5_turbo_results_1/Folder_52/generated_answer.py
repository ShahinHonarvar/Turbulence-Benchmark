
import itertools

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[:8] if ch.isalpha()]
    palindromes = set()
    
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
