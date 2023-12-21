
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    possible_letters = set(english_letters[3:5])
    palindromes = set()

    for combination in itertools.product(possible_letters, repeat=len(possible_letters)):
        word = ''.join(combination)
        word = word.lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
