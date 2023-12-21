
import itertools
import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[2:7])
    palindromes = set()
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
            
    return palindromes
