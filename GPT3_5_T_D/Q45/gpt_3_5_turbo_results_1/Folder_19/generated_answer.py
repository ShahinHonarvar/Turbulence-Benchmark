
import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters, 7):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome.lower())
    return palindromes if palindromes else set()
