
import itertools

def palindromes_between_indices(string):
    letters = [ch.lower() for ch in string[:6] if ch.isalpha()]
    palindromes = set()
    
    for permutation in itertools.permutations(letters, len(letters)):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
