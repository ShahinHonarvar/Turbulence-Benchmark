
from itertools import permutations

def palindromes_between_indices(input_string):
    substr = input_string[5:8]
    char_permutations = permutations(substr)
    possible_palindromes = set()
    
    for perms in char_permutations:
        string = ''.join(perms)
        if string.lower() == string[::-1].lower() and len(string) >= 3:
            possible_palindromes.add(string)
    
    return possible_palindromes
