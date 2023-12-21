
import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = [c for c in string if c.isalpha()]
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, r):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
