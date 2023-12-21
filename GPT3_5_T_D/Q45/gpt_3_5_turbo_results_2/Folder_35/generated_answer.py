
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for combination in itertools.permutations(letters[2:5]):
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
