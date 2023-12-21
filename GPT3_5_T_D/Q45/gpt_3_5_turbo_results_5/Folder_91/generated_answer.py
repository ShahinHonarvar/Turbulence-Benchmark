
from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[2:7] if char.isalpha()]
    if len(letters) < 3:
        return set()

    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
