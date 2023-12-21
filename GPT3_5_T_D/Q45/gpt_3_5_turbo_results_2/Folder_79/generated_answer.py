
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:8] if c.isalpha()]
    letter_permutations = set(itertools.permutations(letters))
    palindromes = set()

    for permutation in letter_permutations:
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
