
import itertools

def palindromes_between_indices(string):
    english_letters = [letter.lower() for letter in string if letter.isalpha()]
    possible_palindromes = set()
    for length in range(3, len(english_letters) + 1):
        palindromes = set("".join(perm).lower() for perm in itertools.permutations(english_letters, length) if "".join(perm).lower() == "".join(perm[::-1]).lower())
        possible_palindromes.update(palindromes)
    return possible_palindromes
