
from itertools import permutations

def palindromes_between_indices(string):
    perm_list = list(permutations(string[0:7], 5))
    palindromes = set()
    for perm in perm_list:
        test_string = ''.join(perm).lower()
        if test_string == test_string[::-1]:
            palindromes.add(test_string)
    return palindromes
