
from itertools import permutations

def palindromes_between_indices(string):
    letters = [x for x in list(string.lower()) if x.isalpha()]
    if len(letters) < 7:
        return set()
    
    possible_palindromes = set()
    for perm in permutations(letters[3:10], 7):
        word = ''.join(perm)
        if word == word[::-1]:
            possible_palindromes.add(word)
    
    return possible_palindromes
