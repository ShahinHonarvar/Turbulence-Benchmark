
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string[2:5] if c.isalpha()]
    combinations = set(itertools.permutations(letters))
    
    palindromes = set()
    for combination in combinations:
        word = ''.join(combination).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
