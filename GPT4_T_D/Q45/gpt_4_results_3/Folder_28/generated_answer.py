
from itertools import permutations

def palindromes_between_indices(string):
    index_string = string[1:6]
    perms = [''.join(p) for p in permutations(index_string)]
    palindromes = set()
    
    for word in perms:
        if len(word) >= 4:
            word_lower = word.lower()
            if word_lower == word_lower[::-1]: 
                palindromes.add(word_lower)
    
    return palindromes
