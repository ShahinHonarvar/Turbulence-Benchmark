
import itertools

def palindromes_between_indices(string):
    letters = [x for x in string[2:7] if x.isalpha()]
    palindromes = set()
    
    for combination in itertools.permutations(letters):
        word = ''.join(combination).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
