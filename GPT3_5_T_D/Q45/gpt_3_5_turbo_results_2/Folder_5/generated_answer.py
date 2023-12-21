
import itertools

def palindromes_between_indices(string):
    english_letters = [letter for letter in string if letter.isalpha()]
    english_letters_range = english_letters[4:9]
    palindromes = set()

    for combination in itertools.permutations(english_letters_range, len(english_letters_range)):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)

    return palindromes
