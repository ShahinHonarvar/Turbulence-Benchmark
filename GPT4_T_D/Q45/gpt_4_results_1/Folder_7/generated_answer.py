
from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:10].lower()
    possible_palindromes = set()

    for i in range(7, len(string)+1):
        for arrangement in permutations(string, i):
            candidate = ''.join(arrangement)
            if candidate == candidate[::-1]:
                possible_palindromes.add(candidate)

    return possible_palindromes
