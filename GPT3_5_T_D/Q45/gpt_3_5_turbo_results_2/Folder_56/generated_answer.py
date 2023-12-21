
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    letters = letters[5:10]
    permutations = set(itertools.permutations(letters))

    palindromes = set()
    for p in permutations:
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)

    return palindromes
