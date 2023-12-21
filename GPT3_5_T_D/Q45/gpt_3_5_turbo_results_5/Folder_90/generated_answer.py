
import itertools

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string if letter.isalpha()]
    letters_range = letters[:6]

    palindromes = set()
    for combination in itertools.permutations(letters_range, len(letters_range)):
        word = "".join(combination)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    
    return palindromes
