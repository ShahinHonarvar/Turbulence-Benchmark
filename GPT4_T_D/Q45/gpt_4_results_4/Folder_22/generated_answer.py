
from itertools import permutations

def palindromes_between_indices(input_string):
    letters_set = set(input_string[5:7].lower())
    all_palindromes = set()

    for letter in letters_set:
        for p in permutations(input_string, 3):
            word = ''.join(p)
            if word == word[::-1]:
                all_palindromes.add(word)

    return all_palindromes
