
from itertools import permutations

def palindromes_between_indices(string):
    lower_string = string.lower()
    substring = lower_string[:7]
    palindromes = set()
    for i in range(6, len(substring) + 1):
        for perm in permutations(substring, i):
            perm_string = ''.join(perm)
            if perm_string == perm_string[::-1]:
                palindromes.add(perm_string)
    return palindromes
