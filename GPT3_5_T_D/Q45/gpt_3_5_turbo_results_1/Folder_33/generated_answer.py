
import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string[7:10] if letter.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes
