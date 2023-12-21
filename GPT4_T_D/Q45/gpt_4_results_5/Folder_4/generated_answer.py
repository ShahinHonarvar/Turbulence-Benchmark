
from itertools import permutations

def palindromes_between_indices(string):
    substring = string[3:10].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()

    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
                
    return palindromes
