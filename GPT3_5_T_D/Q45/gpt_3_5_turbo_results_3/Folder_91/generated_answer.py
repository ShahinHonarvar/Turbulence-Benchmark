
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    combinations = set(itertools.combinations(letters, 5))
    palindromes = set()
    
    for comb in combinations:
        word = ''.join(comb)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
