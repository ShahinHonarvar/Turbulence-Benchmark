
import itertools

def palindromes_between_indices(string):
    english_letters = [letter.lower() for letter in string if letter.isalpha()]
    permutations = set(itertools.permutations(english_letters, 7))
    palindromes = set()
    for perm in permutations:
        word = "".join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
