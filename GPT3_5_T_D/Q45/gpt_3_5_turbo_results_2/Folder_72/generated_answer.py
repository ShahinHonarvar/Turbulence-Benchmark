
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    permutations = set(itertools.permutations(letters, 7))
    palindromes = set()

    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)

    return palindromes
