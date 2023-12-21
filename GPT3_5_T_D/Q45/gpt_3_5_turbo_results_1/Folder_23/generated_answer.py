
import itertools
def palindromes_between_indices(string):
    letters = ''.join(filter(str.isalpha, string[0:7]))
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) < 4:
            continue
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes
