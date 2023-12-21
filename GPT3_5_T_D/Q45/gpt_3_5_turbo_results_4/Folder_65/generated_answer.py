
import itertools

def palindromes_between_indices(string):
    letters = [c.upper() for c in string[:7] if c.isalpha()]
    palindromes = set()

    for perm in itertools.permutations(letters, 7):
        word = ''.join(perm)

        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)

    return palindromes
