
from itertools import permutations

def palindromes_between_indices(string):
    str_range = string[1:5].lower()
    palindromes = set()
    
    for i in range(5, len(str_range) + 1):
        perms = permutations(str_range, i)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
