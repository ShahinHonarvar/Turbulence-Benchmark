
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[3:7] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
