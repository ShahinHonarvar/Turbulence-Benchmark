
import itertools

def palindromes_between_indices(string):
    english_letters = [letter for letter in string if letter.isalpha()]
    english_letters = english_letters[2:8]
    palindromes = set()

    for arrangement in itertools.permutations(english_letters):
        palindrome = ''.join(arrangement).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)

    return palindromes
