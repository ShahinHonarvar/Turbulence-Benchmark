
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[5:10] if ch.isalpha()]
    permutations = list(itertools.permutations(letters))
    palindromes = set()
    
    for perm in permutations:
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
