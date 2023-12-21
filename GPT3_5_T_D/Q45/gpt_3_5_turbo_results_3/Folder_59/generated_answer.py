
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[8:10] if c.isalpha()]
    palindromes = set()
    for comb in itertools.permutations(letters, len(letters)):
        word = ''.join(comb)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
