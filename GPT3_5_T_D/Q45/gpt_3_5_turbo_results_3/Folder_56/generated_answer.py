
import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string[5:10] if ch.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
