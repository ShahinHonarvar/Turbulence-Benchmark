
import itertools


def palindromes_between_indices(string):
    palindromes = set()
    letters = [ch.lower() for ch in string[5:10] if ch.isalpha()]
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes
