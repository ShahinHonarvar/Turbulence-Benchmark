
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:6] if char.isalpha()]
    permutations = list(itertools.permutations(letters))
    palindromes = set()

    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)

    return palindromes
