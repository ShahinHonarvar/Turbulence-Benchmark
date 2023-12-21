 
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    permutations = set(itertools.permutations(english_letters, r=8))
    palindromes = set()

    for perm in permutations:
        word = "".join(perm)[:8].lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    
    return palindromes
