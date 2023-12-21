
from itertools import permutations

def palindromes_between_indices(string):
    letters = string[0:6].lower()
    possible_palindromes = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            candidate = "".join(perm)
            if candidate == candidate[::-1]: 
                possible_palindromes.add(candidate)
    return possible_palindromes
