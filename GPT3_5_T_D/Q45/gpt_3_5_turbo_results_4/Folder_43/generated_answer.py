
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    arr = letters[2:6]
    palindromes = set()
    for perm in itertools.permutations(arr):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
