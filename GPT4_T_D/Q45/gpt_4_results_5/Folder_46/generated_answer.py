
from itertools import permutations

def palindromes_between_indices(string):
    string = string[4:10].lower()
    set_of_palindromes = set()
    for length in range(6, len(string) + 1):
        for perm in permutations(string, length):
            perm_string = ''.join(perm)
            if perm_string == perm_string[::-1]:
                set_of_palindromes.add(perm_string)
    return set_of_palindromes
