
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[2:4] if char.isalpha()]
    if not letters or len(letters) < 3:
        return set()
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
