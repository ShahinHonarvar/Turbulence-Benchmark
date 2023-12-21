
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    letters = letters[2:8]
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = "".join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word.lower())
    return palindromes
