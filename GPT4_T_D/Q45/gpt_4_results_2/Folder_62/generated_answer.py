
from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:9].lower()
    palindromes = set()
    for i in range(7,len(string)+1):
        Permutations = set(permutations(string, i))
        for perm in Permutations:
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes
