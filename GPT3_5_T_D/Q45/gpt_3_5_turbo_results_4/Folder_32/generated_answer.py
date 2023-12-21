
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:8] if c.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if word.lower() == word[::-1].lower() and len(word) >= 5:
            palindromes.add(word)
    return palindromes
