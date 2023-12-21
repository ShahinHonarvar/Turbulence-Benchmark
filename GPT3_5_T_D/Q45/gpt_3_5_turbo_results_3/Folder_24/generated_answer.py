
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string[2:10] if letter.isalpha()]
    possible_palindromes = set()
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            possible_palindromes.add(word)
    return possible_palindromes
