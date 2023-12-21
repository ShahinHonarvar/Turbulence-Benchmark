
import itertools

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    permutations = itertools.permutations(english_letters, len(english_letters))
    palindromes = set()
    for p in permutations:
        word = ''.join(p)[:7]
        if len(word) >= 6 and is_palindrome(word):
            palindromes.add(word)
    return palindromes
