
from itertools import permutations

def palindromes_between_indices(string):
    subset_str = string[:6].lower()
    palindromes = set()
    
    for i in range(6, len(subset_str)+1):
        perms = set(permutations(subset_str, i))
        for word in perms:
            word_str = ''.join(word)
            if word_str == word_str[::-1]:
                palindromes.add(word_str)
    
    return palindromes
