
from itertools import permutations

def palindromes_between_indices(given_string):
    string_segment = given_string[4:9].lower()
    possible_palindromes = set()
    
    for i in range(3, len(string_segment) + 1):
        possible_literals = permutations(string_segment, i)
        for literal in possible_literals:
            arranged_literal = ''.join(literal)
            if arranged_literal == arranged_literal[::-1]:
                possible_palindromes.add(arranged_literal)
    return possible_palindromes
