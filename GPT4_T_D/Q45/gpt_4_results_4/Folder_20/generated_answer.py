
from itertools import permutations

def palindromes_between_indices(string):
    string = string[2:9].lower()
    string = ''.join(ch for ch in string if ch.isalpha())

    palindromes = set()
    for i in range(4, len(string) + 1):
        for perm in permutations(string, i):
            perm_string = ''.join(perm)
            if perm_string == perm_string[::-1]:
                palindromes.add(perm_string)

    return palindromes
