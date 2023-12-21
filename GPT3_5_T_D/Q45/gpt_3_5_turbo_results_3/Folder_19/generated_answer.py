
import itertools

def palindromes_between_indices(string):
    string = string[1:8].lower()
    permutations = set(itertools.permutations(string))
    palindromes = set()
    
    for p in permutations:
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    
    return palindromes
