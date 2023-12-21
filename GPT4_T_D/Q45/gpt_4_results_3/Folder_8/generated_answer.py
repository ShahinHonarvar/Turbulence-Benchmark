
from itertools import permutations 

def palindromes_between_indices(input_string):
    input_string = input_string[1:6].lower()
    possible_palindromes = set()
    for i in range(5, len(input_string)+1):
        perms = [''.join(p) for p in permutations(input_string, i)]
        for p in perms:
            if p == p[::-1]:
                possible_palindromes.add(p)
    return possible_palindromes
