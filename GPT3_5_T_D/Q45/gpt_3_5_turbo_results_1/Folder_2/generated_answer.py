
import itertools

def palindromes_between_indices(string):
    english_letters = [c for c in string if c.isalpha()]
    permutations = itertools.permutations(english_letters, 5)
    palindromes = set()
    
    for perm in permutations:
        word = "".join(perm).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
