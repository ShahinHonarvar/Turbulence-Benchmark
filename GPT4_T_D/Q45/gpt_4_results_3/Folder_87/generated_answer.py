
from itertools import permutations

def palindromes_between_indices(str_val):
    str_val = str_val[3:10].lower()
    str_val = ''.join(filter(str.isalpha, str_val))
    palindromes = set()
    for i in range(3, len(str_val) + 1):
        perms = list(set(permutations(str_val, i)))
        for perm in perms:
            word = ''.join(perm) 
            if word == word[::-1]: 
                palindromes.add(word)
    return palindromes
