
from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string[2:8].lower()
    possible_strings = [''.join(p) for p in permutations(input_string)]
    palindromes = set()
    for string in possible_strings:
        if string == string[::-1] and len(string) >= 3:
            palindromes.add(string)
    return palindromes
