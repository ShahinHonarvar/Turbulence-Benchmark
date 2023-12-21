
import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()

    for perm in itertools.permutations(letters, 5):
        word = ''.join([perm[i] for i in range(len(perm))]).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)

    return palindromes
